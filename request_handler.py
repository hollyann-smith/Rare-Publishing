from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from views.user_requests import create_user, get_all_users, get_single_user, login_user, update_user
from views.post_requests import get_all_posts, create_post, delete_post, update_post, get_single_post
from views.category_requests import get_categories, create_category, delete_category, get_single_category
from urllib.parse import urlparse
from views import *
from urllib.parse import urlparse, parse_qs


class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""

    def parse_url(self, path):
        """Parse the url into the resource and id"""
        parsed_url = urlparse(path)
        path_params = self.path.split('/')
        resource = path_params[1]
        if '?' in resource:
            param = resource.split('?')[1]
            resource = resource.split('?')[0]
            pair = param.split('=')
            key = pair[0]
            value = pair[1]
            return (resource, key, value)
        else:
            id = None
            try:
                id = int(path_params[2])
            except (IndexError, ValueError):
                pass
            return (resource, id)

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the OPTIONS headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        self._set_headers(200)

        response = {}

        parsed = self.parse_url(self.path)

        if '?' not in self.path:
            ( resource, id ) = parsed

            # It's an if..else statement
            if resource == 'users':
                if id is not None:
                    response = get_single_user(id)
                    self._set_headers(200)
                else:
                    response = get_all_users()
                    self._set_headers(200)  
            if resource == "posts":
                if id is not None:
                    response = get_single_post(id)
                else:
                    response = get_all_posts()
            if resource == "categories":
                if id is not None:
                    response = get_single_category(id)
                else: 
                    response = get_categories()
            if resource == "comments":
                response = get_comments_by_post(id)                 
            else:
                (resource, query) = parsed

            self.wfile.write(json.dumps(response).encode())
            
        else: # There is a ? in the path, run the query param functions
            (resource, query, value) = self.parse_url(self.path)


    def do_POST(self):
        """Make a post request to the server"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = json.loads(self.rfile.read(content_len))
        response = ''
        resource, _ = self.parse_url(self.path)
    
        new_item = None
        
        if resource == "posts":
            new_item = create_post(post_body)
            self.wfile.write(json.dumps(new_item).encode())
        elif resource == 'login':
            response = login_user(post_body)
            self.wfile.write(response.encode())
        elif resource == 'register':
            response = create_user(post_body)
        elif resource == 'categories':
            new_item = create_category(post_body)
            self.wfile.write(response.encode())
        elif resource == "comments":
            new_item = create_comment(post_body)
            self.wfile.write(response.encode())


    def do_PUT(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)
        
        success = False

        if resource == "posts":
            success = update_post(id, post_body)
        elif resource == "comments":
            success = update_comment(id, post_body)
        elif resource == "users":
            success = update_user(id,post_body)
            
        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        self.wfile.write("".encode())
        self._set_headers(204)
            

    def do_DELETE(self):
        self._set_headers(204)

        (resource, id) = self.parse_url(self.path)

        if resource == "posts":
            delete_post(id)
        elif resource == "comments":
            delete_comment(id)
        elif resource == 'categories':
            delete_category(id)
            
        self.wfile.write("".encode())


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
