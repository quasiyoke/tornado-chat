(function(){
	var domainPort = /\w+:\/\/([\w\.\:\d]+)/.exec(document.documentURI)[1];
	var socket = new WebSocket('ws://' + domainPort + '/socket/');
	socket.onopen = function(){
		socket.send(JSON.stringify({
			type: 'set_color',
			color: COLOR
		}));
	};
	
	window.addEventListener('load', function(){
		var bodyWidth = document.body.getClientRects()[0].width;

		var formWrap = document.getElementsByClassName('form-wrap')[0];
		var formWrapWidth = formWrap.getClientRects()[0].width;
		formWrap.style.left = (bodyWidth - formWrapWidth) / 2 + 'px';

		var messages = document.getElementsByClassName('messages')[0];
		
		socket.onmessage = function(e){
			var message = JSON.parse(e.data);
			var text;
			if('user_come' === message.type){
				text = 'Meet new user';
			}else if('user_gone' === message.type){
				text = 'User gone';
			}
			var el = document.createElement('li');
			el.appendChild(document.createTextNode(text));
			el.style.color = '#' + message.color;
			messages.appendChild(el);
		};
	});
})();
