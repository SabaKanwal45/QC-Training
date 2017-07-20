
6- Debugging JavaScript.

There is some JavaScript code at end of this document, you will
have to correct it. Learn how to use Chrome’s debugger and
show us what did you learn.
Deadline is 11:59 PM.
What's the problem with following JavaScript, what is the best way to solve it?

var ali = {

 	firstname: 'ali',

 	say_hi: function(firstname) {

    alert("Greetings " + firstname + ", you are talking to " + this.firstname + "!");

  }

};


var some_ref = ali.say_hi; some_ref("Sabir"); 
