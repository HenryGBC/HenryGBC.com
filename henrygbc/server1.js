var http = required('http');

http.createServer(function(req, res){
	res.writeHead(200, {'Content-type': 'text/plain'});
	res.end("Servidor 1\n");

}).listen(3000, '127.0.0.1');

console.log('Server Runing at http://127.0.0.1:3000');