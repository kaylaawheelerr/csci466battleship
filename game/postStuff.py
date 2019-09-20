def do_POST(self):
        self.send_response(202)
        content = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content)
        post_data = post_data.decode("utf-8")
        coords=re.findall(r'\d+',post_data)
        x = coords[0]
        y = coords[1]
        print("x = "+ x, " y = " + y)