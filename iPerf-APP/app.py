from bottle import Bottle, run, request
import iperf3

app = Bottle()

@app.route('/')
def home():
    return '''
    <h1>iperf3 Test</h1>
    <form action="/start-test" method="post">
        <label>Mode:</label>
        <select name="mode" onchange="toggleServerField(this.value)" required>
            <option value="server">Server</option>
            <option value="client">Client</option>
        </select><br><br>
        <div id="server-field" style="display:none;">
            <label>Server IP:</label>
            <input type="text" name="server"><br><br>
        </div>
        <label>Test Duration (seconds):</label>
        <input type="number" name="duration" value="10"><br><br>
        <label>Use UDP:</label>
        <input type="checkbox" name="udp"><br><br>
        <input type="submit" value="Start Test">
    </form>
    <script>
        function toggleServerField(value) {
            const serverField = document.getElementById('server-field');
            if (value === 'client') {
                serverField.style.display = 'block';
            } else {
                serverField.style.display = 'none';
            }
        }
    </script>
    '''

@app.route('/start-test', method='POST')
def start_test():
    mode = request.forms.get('mode')
    duration = int(request.forms.get('duration'))
    use_udp = 'udp' in request.forms

    if mode == 'server':
        server = iperf3.Server()
        try:
            server.run()
            if result.error:
                return f"<h2>Error: {result.error}</h2>"
            return '''
            <h2>iperf3 Server Started</h2>
            <p>The server is now running and ready to accept connections.</p>
            <a href="/">Back</a>
            '''
        except Exception as e:
            return f"<h2>Error: {str(e)}</h2>"
    elif mode == 'client':
        server_ip = request.forms.get('server')
        if not server_ip:
            return "<h2>Error: Server IP is required for client mode.</h2>"
        client = iperf3.Client()
        client.server_hostname = server_ip
        client.duration = duration
        client.protocol = 'udp' if use_udp else 'tcp'
        try:
            result = client.run()
            if result.error:
                return f"<h2>Error: {result.error}</h2>"
            return f'''
            <h2>iperf3 Test Results</h2>
            <p>Server: {server_ip}</p>
            <p>Duration: {duration} seconds</p>
            <p>Protocol: {'UDP' if use_udp else 'TCP'}</p>
            <p>Throughput: {result.sent_Mbps:.2f} Mbps</p>
            <a href="/">Run Another Test</a>
            '''
        except Exception as e:
            return f"<h2>Error: {str(e)}</h2>"

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8080)
