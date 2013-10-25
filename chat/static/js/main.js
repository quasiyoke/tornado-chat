(function(){
	window.addEventListener('load', function(){
		var body = document.getElementsByTagName('body')[0];
		var bodyWidth = body.getClientRects()[0].width;

		var formWrap = document.getElementsByClassName('form-wrap')[0];
		var formWrapWidth = formWrap.getClientRects()[0].width;
		formWrap.style.left = (bodyWidth - formWrapWidth) / 2 + 'px';		
	});
})();
