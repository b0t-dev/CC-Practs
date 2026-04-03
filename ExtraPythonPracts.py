Python Cloud Practical
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
class CloudService(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_url = urlparse(self.path)
        params = parse_qs(parsed_url.query)

        if parsed_url.path == "/":
            self.show_form()

        elif parsed_url.path == "/process":
            self.process_request(params)

    def show_form(self):
        html = """
        <html>
        <body>
            <h2>Cloud Computing Simulation</h2>
            <form action="/process" method="get">
                Enter your name:
                <input type="text" name="name"><br><br>

                Enter number of users:
                <input type="number" name="users"><br><br>

                <input type="submit" value="Send Request">
            </form>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

    def process_request(self, params):
        name = params.get("name", ["Guest"])[0]
        users = int(params.get("users", [1])[0])

        if users <= 10:
            response = "Low Load"
        elif users <= 50:
            response = "Medium Load"
        else:
            response = "High Load – Scaling Needed!"

        result = f"""
        <html>
        <body>
            <h3>Hello {name}</h3>
            <p>Users accessing service: {users}</p>
            <p>System Status: <b>{response}</b></p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(result.encode())

server = HTTPServer(("0.0.0.0", 8000), CloudService)
print("Cloud service running on port 8000...")
server.serve_forever()

factorial python cloud
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class CloudService(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_url = urlparse(self.path)
        params = parse_qs(parsed_url.query)

        if parsed_url.path == "/":
            self.show_form()

        elif parsed_url.path == "/process":
            self.process_request(params)

    def show_form(self):
        html = """
        <html>
        <body>
            <h2>Factorial Calculator (Cloud Simulation)</h2>
            <form action="/process" method="get">
                Enter your name:
                <input type="text" name="name"><br><br>

                Enter a number:
                <input type="number" name="num"><br><br>

                <input type="submit" value="Calculate">
            </form>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

    def process_request(self, params):
        name = params.get("name", ["Guest"])[0]
        num = int(params.get("num", [0])[0])

        # Factorial logic
        factorial = 1
        if num < 0:
            result_value = "Factorial not defined for negative numbers"
        else:
            for i in range(1, num + 1):
                factorial *= i
            result_value = factorial

        result = f"""
        <html>
        <body>
            <h3>Hello {name}</h3>
            <p>Entered Number: {num}</p>
            <p>Factorial: <b>{result_value}</b></p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(result.encode())

server = HTTPServer(("0.0.0.0", 8000), CloudService)
print("Server running on port 8000...")
server.serve_forever()

fibonacci python cloud
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class CloudService(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_url = urlparse(self.path)
        params = parse_qs(parsed_url.query)

        if parsed_url.path == "/":
            self.show_form()

        elif parsed_url.path == "/process":
            self.process_request(params)

    def show_form(self):
        html = """
        <html>
        <body>
            <h2>Fibonacci Series Calculator (Cloud Simulation)</h2>
            <form action="/process" method="get">
                Enter your name:
                <input type="text" name="name"><br><br>

                Enter number of terms:
                <input type="number" name="num"><br><br>

                <input type="submit" value="Generate">
            </form>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

    def process_request(self, params):
        name = params.get("name", ["Guest"])[0]
        num = int(params.get("num", [0])[0])

        # Fibonacci logic
        fib_series = []
        a, b = 0, 1

        if num <= 0:
            fib_series = "Enter a positive number"
        else:
            for _ in range(num):
                fib_series.append(a)
                a, b = b, a + b

        result = f"""
        <html>
        <body>
            <h3>Hello {name}</h3>
            <p>Number of terms: {num}</p>
            <p>Fibonacci Series: <b>{fib_series}</b></p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(result.encode())

server = HTTPServer(("0.0.0.0", 8000), CloudService)
print("Server running on port 8000...")
server.serve_forever()

prime no python cloud
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class CloudService(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_url = urlparse(self.path)
        params = parse_qs(parsed_url.query)

        if parsed_url.path == "/":
            self.show_form()

        elif parsed_url.path == "/process":
            self.process_request(params)

    def show_form(self):
        html = """
        <html>
        <body>
            <h2>Prime Number Checker (Cloud Simulation)</h2>
            <form action="/process" method="get">
                Enter your name:
                <input type="text" name="name"><br><br>

                Enter a number:
                <input type="number" name="num"><br><br>

                <input type="submit" value="Check">
            </form>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

    def process_request(self, params):
        name = params.get("name", ["Guest"])[0]
        num = int(params.get("num", [0])[0])

        # Prime number logic
        if num <= 1:
            result_value = "Not a Prime Number"
        else:
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                result_value = "Prime Number"
            else:
                result_value = "Not a Prime Number"

        result = f"""
        <html>
        <body>
            <h3>Hello {name}</h3>
            <p>Entered Number: {num}</p>
            <p>Result: <b>{result_value}</b></p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(result.encode())

server = HTTPServer(("0.0.0.0", 8000), CloudService)
print("Server running on port 8000...")
server.serve_forever()

palindrome python cloud
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class CloudService(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_url = urlparse(self.path)
        params = parse_qs(parsed_url.query)

        if parsed_url.path == "/":
            self.show_form()

        elif parsed_url.path == "/process":
            self.process_request(params)

    def show_form(self):
        html = """
        <html>
        <body>
            <h2>Palindrome Checker (Cloud Simulation)</h2>
            <form action="/process" method="get">
                Enter your name:
                <input type="text" name="name"><br><br>

                Enter a value:
                <input type="text" name="value"><br><br>

                <input type="submit" value="Check">
            </form>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

    def process_request(self, params):
        name = params.get("name", ["Guest"])[0]
        value = params.get("value", [""])[0]

        # Palindrome logic
        if value == value[::-1]:
            result_value = "Palindrome"
        else:
            result_value = "Not a Palindrome"

        result = f"""
        <html>
        <body>
            <h3>Hello {name}</h3>
            <p>Entered Value: {value}</p>
            <p>Result: <b>{result_value}</b></p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(result.encode())

server = HTTPServer(("0.0.0.0", 8000), CloudService)
print("Server running on port 8000...")
server.serve_forever()

Celcius to farenheit python cloud
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class CloudService(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_url = urlparse(self.path)
        params = parse_qs(parsed_url.query)

        if parsed_url.path == "/":
            self.show_form()

        elif parsed_url.path == "/process":
            self.process_request(params)

    def show_form(self):
        html = """
        <html>
        <body>
            <h2>Temperature Converter (Cloud Simulation)</h2>
            <form action="/process" method="get">
                Enter your name:
                <input type="text" name="name"><br><br>

                Enter temperature in Celsius:
                <input type="number" name="temp"><br><br>

                <input type="submit" value="Convert">
            </form>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

    def process_request(self, params):
        name = params.get("name", ["Guest"])[0]
        temp = float(params.get("temp", [0])[0])

        # Celsius to Fahrenheit logic
        fahrenheit = (temp * 9/5) + 32

        result = f"""
        <html>
        <body>
            <h3>Hello {name}</h3>
            <p>Temperature in Celsius: {temp}°C</p>
            <p>Temperature in Fahrenheit: <b>{fahrenheit}°F</b></p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(result.encode())

server = HTTPServer(("0.0.0.0", 8000), CloudService)
print("Server running on port 8000...")
server.serve_forever()

Farenheit to celcius python cloud
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class CloudService(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_url = urlparse(self.path)
        params = parse_qs(parsed_url.query)

        if parsed_url.path == "/":
            self.show_form()

        elif parsed_url.path == "/process":
            self.process_request(params)

    def show_form(self):
        html = """
        <html>
        <body>
            <h2>Temperature Converter (Cloud Simulation)</h2>
            <form action="/process" method="get">
                Enter your name:
                <input type="text" name="name"><br><br>

                Enter temperature in Fahrenheit:
                <input type="number" name="temp"><br><br>

                <input type="submit" value="Convert">
            </form>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

    def process_request(self, params):
        name = params.get("name", ["Guest"])[0]
        temp = float(params.get("temp", [0])[0])

        # Fahrenheit to Celsius logic
        celsius = (temp - 32) * 5/9

        result = f"""
        <html>
        <body>
            <h3>Hello {name}</h3>
            <p>Temperature in Fahrenheit: {temp}°F</p>
            <p>Temperature in Celsius: <b>{celsius}°C</b></p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(result.encode())

server = HTTPServer(("0.0.0.0", 8000), CloudService)
print("Server running on port 8000...")
server.serve_forever()

Even or odd python cloud 
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class CloudService(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_url = urlparse(self.path)
        params = parse_qs(parsed_url.query)

        if parsed_url.path == "/":
            self.show_form()

        elif parsed_url.path == "/process":
            self.process_request(params)

    def show_form(self):
        html = """
        <html>
        <body>
            <h2>Even or Odd Checker (Cloud Simulation)</h2>
            <form action="/process" method="get">
                Enter your name:
                <input type="text" name="name"><br><br>

                Enter a number:
                <input type="number" name="num"><br><br>

                <input type="submit" value="Check">
            </form>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

    def process_request(self, params):
        name = params.get("name", ["Guest"])[0]
        num = int(params.get("num", [0])[0])

        # Even / Odd logic
        if num % 2 == 0:
            result_value = "Even Number"
        else:
            result_value = "Odd Number"

        result = f"""
        <html>
        <body>
            <h3>Hello {name}</h3>
            <p>Entered Number: {num}</p>
            <p>Result: <b>{result_value}</b></p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(result.encode())

server = HTTPServer(("0.0.0.0", 8000), CloudService)
print("Server running on port 8000...")
server.serve_forever()

Amstrong Number python cloud
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class CloudService(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_url = urlparse(self.path)
        params = parse_qs(parsed_url.query)

        if parsed_url.path == "/":
            self.show_form()

        elif parsed_url.path == "/process":
            self.process_request(params)

    def show_form(self):
        html = """
        <html>
        <body>
            <h2>Armstrong Number Checker (Cloud Simulation)</h2>
            <form action="/process" method="get">
                Enter your name:
                <input type="text" name="name"><br><br>

                Enter a number:
                <input type="number" name="num"><br><br>

                <input type="submit" value="Check">
            </form>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

    def process_request(self, params):
        name = params.get("name", ["Guest"])[0]
        num = int(params.get("num", [0])[0])

        # Armstrong logic
        temp = num
        power = len(str(num))
        total = 0

        while temp > 0:
            digit = temp % 10
            total += digit ** power
            temp //= 10

        if total == num:
            result_value = "Armstrong Number"
        else:
            result_value = "Not an Armstrong Number"

        result = f"""
        <html>
        <body>
            <h3>Hello {name}</h3>
            <p>Entered Number: {num}</p>
            <p>Result: <b>{result_value}</b></p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(result.encode())

server = HTTPServer(("0.0.0.0", 8000), CloudService)
print("Server running on port 8000...")
server.serve_forever()

GCD python cloud
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class CloudService(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_url = urlparse(self.path)
        params = parse_qs(parsed_url.query)

        if parsed_url.path == "/":
            self.show_form()

        elif parsed_url.path == "/process":
            self.process_request(params)

    def show_form(self):
        html = """
        <html>
        <body>
            <h2>GCD Calculator (Cloud Simulation)</h2>
            <form action="/process" method="get">
                Enter your name:
                <input type="text" name="name"><br><br>

                Enter first number:
                <input type="number" name="a"><br><br>

                Enter second number:
                <input type="number" name="b"><br><br>

                <input type="submit" value="Calculate">
            </form>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

    def process_request(self, params):
        name = params.get("name", ["Guest"])[0]
        a = int(params.get("a", [0])[0])
        b = int(params.get("b", [0])[0])

        # GCD logic (Euclidean Algorithm)
        x, y = a, b
        while y != 0:
            x, y = y, x % y

        gcd = x

        result = f"""
        <html>
        <body>
            <h3>Hello {name}</h3>
            <p>First Number: {a}</p>
            <p>Second Number: {b}</p>
            <p>GCD: <b>{gcd}</b></p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(result.encode())

server = HTTPServer(("0.0.0.0", 8000), CloudService)
print("Server running on port 8000...")
server.serve_forever()

Krishnamurthy number python cloud
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class CloudService(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_url = urlparse(self.path)
        params = parse_qs(parsed_url.query)

        if parsed_url.path == "/":
            self.show_form()

        elif parsed_url.path == "/process":
            self.process_request(params)

    def show_form(self):
        html = """
        <html>
        <body>
            <h2>Krishnamurthy Number Checker (Cloud Simulation)</h2>
            <form action="/process" method="get">
                Enter your name:
                <input type="text" name="name"><br><br>

                Enter a number:
                <input type="number" name="num"><br><br>

                <input type="submit" value="Check">
            </form>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

    def process_request(self, params):
        name = params.get("name", ["Guest"])[0]
        num = int(params.get("num", [0])[0])

        # Function to calculate factorial
        def factorial(n):
            fact = 1
            for i in range(1, n + 1):
                fact *= i
            return fact

        # Krishnamurthy logic
        temp = num
        total = 0

        while temp > 0:
            digit = temp % 10
            total += factorial(digit)
            temp //= 10

        if total == num:
            result_value = "Krishnamurthy Number"
        else:
            result_value = "Not a Krishnamurthy Number"

        result = f"""
        <html>
        <body>
            <h3>Hello {name}</h3>
            <p>Entered Number: {num}</p>
            <p>Result: <b>{result_value}</b></p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(result.encode())

server = HTTPServer(("0.0.0.0", 8000), CloudService)
print("Server running on port 8000...")
server.serve_forever()

Reverse number python cloud
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class CloudService(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_url = urlparse(self.path)
        params = parse_qs(parsed_url.query)

        if parsed_url.path == "/":
            self.show_form()

        elif parsed_url.path == "/process":
            self.process_request(params)

    def show_form(self):
        html = """
        <html>
        <body>
            <h2>Reverse Number (Cloud Simulation)</h2>
            <form action="/process" method="get">
                Enter your name:
                <input type="text" name="name"><br><br>

                Enter a number:
                <input type="number" name="num"><br><br>

                <input type="submit" value="Reverse">
            </form>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

    def process_request(self, params):
        name = params.get("name", ["Guest"])[0]
        num = int(params.get("num", [0])[0])

        # Reverse number logic
        reverse = int(str(num)[::-1])

        result = f"""
        <html>
        <body>
            <h3>Hello {name}</h3>
            <p>Entered Number: {num}</p>
            <p>Reversed Number: <b>{reverse}</b></p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(result.encode())

server = HTTPServer(("0.0.0.0", 8000), CloudService)
print("Server running on port 8000...")
server.serve_forever()
