const http = require('http');
const port = 3000;

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Backend 2\n');
});

server.listen(port, () => {
  console.log(`Backend 2 running on port ${port}`);
});
