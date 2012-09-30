from bottle import route, run, get, post, request
from dropbox import client, rest, session
import dropbox
import bottle

APP_KEY = 'twi5qolo5zsoo35'
APP_SECRET = 'hidqvr44h9v15th'
ACCESS_TYPE = 'app_folder'
TOKEN_STORE = {}

def get_session():
    return session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)

def get_client(access_token):
    sess = get_session()
    sess.set_token(access_token.key, access_token.secret)
    return client.DropboxClient(sess)

def get_auth_url():
    global request_token
    sess = get_session()
    request_token = sess.obtain_request_token()
    bottle.request.headers['host']
    callback_url = "http://" + bottle.request.headers['host'] + "/callback"
    return sess.build_authorize_url(request_token, callback_url)

def get_client_metadata(path):
    global access_token
    c = get_client(access_token)
    return c.metadata(path)

def get_client_file_and_metadata(path):
    global access_token
    c = get_client(access_token)
    return c.get_file_and_metadata(path)

def put_client_file(path, file_name,  parent_rev):
    global access_token
    c = get_client(access_token)
    file_obj = open(file_name, 'r')
    c.put_file(path, file_obj, True, parent_rev)
    file_obj.close()
    return None

def get_info(path):
    prev_path = path[:path.rfind('/')]
    root_url = "http://" + bottle.request.headers['host'] + '/directory/'
    prev_path_url = root_url + prev_path
    
    info = """
<p><b>Viewing Contents of : {0}</b></p>
<p><a href = "{2}"><b>Go up to: {1}</b></a></p>
<p><a href = "{3}"><b>Go back to root</b></a></p>
    """.format(path, prev_path, prev_path_url, root_url)

    return info

def render_directory(metadata):
    assert 'contents' in metadata, "Directory must have contents in it!"

    html = get_info(metadata['path'])

    contents = metadata['contents']
    dirs = [d for d in contents if d['is_dir']]
    files = [d for d in contents if not d['is_dir']]

    html += '<table border = "0"'
    if dirs!= []:
        html += """<tr>
                   <th>Folder Name</th>
                   <th>&nbsp</th>
                   <th>Last Modified</th>
                   </tr>"""
        for entry in dirs:
            path = entry['path']
            dir_url = "http://" + bottle.request.headers['host'] + '/directory' + entry['path']
            html += '<tr><td><a href="{3}">{0}</a></td><td>{1}</td><td>{2}</td></tr>'.format(path[path.rfind('/')+1:], '&nbsp', entry['modified'], dir_url)
    if files != []:
        html += """<tr>
                   <th>File Name</th>
                   <th>Size</th>
                   <th>Last Modified</th>
                   </tr>"""
        for entry in files:
            path = entry['path']
            file_url = "http://" + bottle.request.headers['host'] + '/file' + entry['path']
            html += '<tr><td><a href="{3}">{0}</a></td><td>{1}</td><td>{2}</td></tr>'.format(path[path.rfind('/')+1:], entry['size'], entry['modified'],file_url)

    html += '</table>'
    return html
            
@route('/')
def hello():
    page = '<html><head><title>Your Page Title</title><meta http-equiv="REFRESH" content="0;url=' + get_auth_url() + '"></head><body>Redirecting to dropbox authentication...</body></html>'
    return page

@route('/callback')
def callback():
    global request_token, access_token
    sess = get_session()
    access_token = sess.obtain_access_token(request_token)
    dir_url = "http://" + bottle.request.headers['host'] + "/directory/"
    return '<html></head><meta http-equiv="REFRESH" content="0;url='+ dir_url +'"></head></html>'
    

@route('/directory<path:path>')
def directory(path):
    metadata = get_client_metadata(path)

    page = '<html><body>' + render_directory(metadata) + '</body></html>'
    return page

@get('/file<path:path>')
def edit_file(path):
    f, metadata = get_client_file_and_metadata(path)
    file_url = "/submit" + path
    page = """
<html>
<body>
{0}
<form method="POST" action = "{2}">
<textarea cols = "80" rows = "35" name = "text_editor">
{1}
</textarea>
<input type = "submit" value = "Save">
<input type = "hidden" name = "rev" value = "{3}">
</form>
</body>
</html>
    """.format(get_info(path), f.read(), file_url, metadata['rev'])
    return page

@post('/submit<path:path>')
def submit_file(path):
    file_url = "http://" + bottle.request.headers['host'] + "/file" + path
    parent_rev = request.forms.get('rev')
    temp_file = open('temp', 'w')
    temp_file.write(request.forms.get('text_editor'))
    temp_file.close()
    put_client_file(path, 'temp', parent_rev)
    temp_file.close()
    return '<html></head><meta http-equiv="REFRESH" content="0;url='+ file_url +'"></head></html>'

run(host='localhost', port=8080, debug=True)
#run(host='192.168.0.1', port=80)
