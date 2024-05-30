import json
from http.server import HTTPServer
from nss_handler import HandleRequests, status


from views import retrieve_post, list_posts, login_user



class JSONServer(HandleRequests):
    def do_GET(self):

        response_body = ""
        url = self.parse_url(self.path)

        if url["requested_resource"] == "posts":
            if url["pk"] != 0:
                response_body = retrieve_post(url)
                return self.response(response_body, status.HTTP_200_SUCCESS.value)
            response_body = list_posts(url)
            return self.response(response_body, status.HTTP_200_SUCCESS.value)


    def do_POST(self):

        if self.path == '/login':

            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            user_data = json.loads(body)
            print(user_data)
            response = login_user(user_data)
            print(response)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        else:
            self.send_error(404)

def main():
    host = ""
    port = 8000
    HTTPServer((host, port), JSONServer).serve_forever()


if __name__ == "__main__":
    main()
