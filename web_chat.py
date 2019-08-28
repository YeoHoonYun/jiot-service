import email_to

server = email_to.EmailServer('demo.jiguem.com', 587, 'iot.jiguem@gmail.com', 'jiguem!')

message = server.message()
message.add('# Oh boy, something went wrong!')
message.add('- The server had a hiccup')
message.add('- The power went out')
message.add('- Blame it on a rogue backhoe')
message.style = 'h1 { color: red}'

message.send('cjswo9207@naver.com', 'Things did not occur as expected')