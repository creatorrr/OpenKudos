var form=document.getElementById('theForm');
var formClient = {};
	formClient.DONE_STATE = 4;
	formClient.ERROR_STATE = 0;

	formClient.getXmlHttpRequest = function() {
			if (window.XMLHttpRequest) {
			return new XMLHttpRequest();
			}
		else if (window.ActiveXObject) {
			try {
				return new ActiveXObject('Msxml2.XMLHTTP');
				}
			catch(e) {
				return new ActiveXObject('Microsoft.XMLHTTP');
				}
			}
		return null;
		};

    formClient.submitData = function() {
        var req = this.getXmlHttpRequest();
		if (!req) {
		form.submit.click();
		}
		
		req.onreadystatechange = function() {};

		var params = '';			// build the query parameter string
		params += '&' + document.getElementById('entry_0').name + '=' + escape(document.getElementById('entry_0').value);
		params += '&' + document.getElementById('entry_1').name + '=' + escape(document.getElementById('entry_1').value);
		params += '&' + document.getElementById('entry_2').name + '=' + escape(document.getElementById('entry_2').value);
		params += '&' + document.getElementById('entry_4').name + '=' + escape(document.getElementById('entry_4').value);
		params += '&' + document.getElementById('entry_6').name + '=' + escape(document.getElementById('entry_6').value);


		// send the request and tell the user.
		req.open(form.method, form.action, true);
		req.setRequestHeader('Content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
		req.setRequestHeader('Content-length', params.length);
		req.setRequestHeader('Connection', 'close');
		req.send(params);

		return false;
    };
    
var query = {};
location.search.replace( /[A-Z0-9]+?=(\w*)/gi, function(a) {
	query[ a.split( '=' ).shift() ] = a.split( '=' ).pop();
} );    

var refField = document.getElementById('entry_6');
refField.value = query.refer || "[No one in Particular]";

function setReference(name){
    var refField = document.getElementById('entry_6');
    refField.value = name;
    return true;
}
