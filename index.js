var os = require('os')
var http = require('http')


function handleRequest(req, res) {
        res.setHeader('Content-Type','text/plain');
        res.write('Hello World! ' + os.hostname())
        res.end()
}
