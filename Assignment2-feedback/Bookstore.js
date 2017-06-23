/* Book Store Implementation Two sides
-admin
-user
admin is able to add new books, view books, view users
user is able to signup, signin,view books, search books, Buy Books,logout
*/

//Book Objects Prototype
function Books(isbn, btitle, author, edition, price, quantity)
{
    this.isbn = isbn;
    this.btitle = btitle;
    this.author = author;
    this.edition = edition;
    this.price = price;
    this.quantity = quantity;
}
/*Checks local storage for Books --if local storage not defined initialize it
with some given books and add it to storage else get books from storage
*/
book_storage=localStorage.getItem("AllBook");
if(typeof book_storage=='undefined' || book_storage==null){
    var allBooks = [];
    var isbn_no=1;
    var book = new Books(isbn_no,"oop","abc",2,200,5);
    allBooks.push(book);
    isbn_no+=1;
    book = new Books(isbn_no,"DS","abc",2,100,5);
    allBooks.push(book);
    isbn_no+=1;
    book = new Books(isbn_no,"SE","abc",2,150,5);
    allBooks.push(book);
    isbn_no+=1;
    book = new Books(isbn_no,"programming","xyz",2,250,5);
    allBooks.push(book);
    isbn_no+=1;
    book = new Books(isbn_no,"english","amjad",2,220,5);
    allBooks.push(book);
    isbn_no+=1;
    book = new Books(isbn_no,"Urdu","Ghulam Rasool",2,250,5);
    allBooks.push(book);
    isbn_no+=1;
    // Set local storage for Books
    var mybook = JSON.stringify(allBooks);
    localStorage.setItem('AllBook', mybook);
    //alert(" ALL"+ allbooks);
}//
else
{
    //get Books from Local Storage
    var mybook=localStorage.getItem('AllBook');
    allBooks= JSON.parse(mybook);
};
// Status Prototype that's added when a user Buy a book
function Notification(usrid, usrname,bktitle,bkauthor,paidamount)
{
   this.usrid=usrid;
   this.usrname=usrname;
   this.bktitle=bktitle;
   this.bkauthor=bkauthor;
   this.paidamount=paidamount;
}
/*Checks local storage for Status or notifications --if local storage not defined initialize it
with some given notification and add it to storage else get notifications from storage
*/
notification_storage=localStorage.getItem("notification");
if(typeof notification_storage=='undefined'|| notification_storage==null){
    var allnoti = [];
    var noti = new Notification(1,"huma","oop","abc",200);
    allnoti.push(noti);
    var mynoti = JSON.stringify(allnoti);
    localStorage.setItem("notification", mynoti);
}
else
{
    var noti=localStorage.getItem('notification');
    allnoti= JSON.parse(noti);
};
//User Prototype
function User(userid,username, userpassword, email, cardno, amount)
{
    this.userid=userid;
    this.username = username;
    this.userpassword = userpassword;
    this.email = email;
    this.cardno = cardno;
    this.amount = amount;
}
/*Checks local storage for Users --if local storage not defined initialize it
with some given users and add it to storage else get users from storage
*/
user_storage=localStorage.getItem("AllUser");
if(typeof user_storage=='undefined' || user_storage==null){
    var allUsers = [];
    var user1= new User(1,"huma",123,"huma@gmail.com",213456,1000);
    allUsers.push(user1);
    user1 = new User(2,"maleeha",456,"maleeha@gmail.com",215367,500);
    allUsers.push(user1);
    user1 = new User(3,"fazila",678,"fazila@gmail.com",317685,2000);
    allUsers.push(user1);
    user1 = new User(4,"muzna",910,"muzna@gmail.com",245987,5000);
    allUsers.push(user1);
    user1 = new User(5,"munaza",112,"munaza@gmail.com",287956,7000);
    allUsers.push(user1);
    user1= new User(6,"komal",115,"komal@gmail.com",267986,5000);
    allUsers.push(user1);
    // Sets Storage for Users
    var myuser = JSON.stringify(allUsers);
    localStorage.setItem('AllUser', myuser);
}
else
{
    // Get Users from Storage
    var myuser=localStorage.getItem('AllUser');
    allUsers= JSON.parse(myuser);
};
// Takes a parameter and validates if its defined and its value is not null
function validateParameter(input_para)
{
    if (typeof input_para == 'undefined' || input_para==null)
    return false;
    else
    return true;
}
 //This method returns index of a given book
Books.prototype.getbookindex=function()
{
    var mybook=localStorage.getItem('AllBook');
    allBooks= JSON.parse(mybook);
    for(var i=0;i<allBooks.length;i++)
    {
        if(allBooks[i].btitle==this.btitle && allBooks[i].author==this.author)
        {
            return i;
        }
    }
    return false;
};
// This Method Returns Copies available of the given Book
Books.prototype.getbookquantity=function()
{
    var mybook=localStorage.getItem('AllBook');
    allBooks= JSON.parse(mybook);
    index=this.getbookindex();
    if(index!=false)
    {
        return allBooks[index].quantity;
    }
    else
    return false;
};
//Checks if Book already in storage
Books.prototype.IsalreadyExist = function()
{
    var mybook=localStorage.getItem('AllBook');
    allBooks= JSON.parse(mybook);
    for(var i=0;i<allBooks.length;i++)
    {
    //alert(allBooks[i].btitle+"  "+this.btitle);
        if(allBooks[i].btitle==this.btitle && allBooks[i].author==this.author)
        {
            //alert(this.btitle);
            return true;
        }
    }
    return false;
};
// This method add the given book to storage
Books.prototype.addbook = function ()
{
    var mybook=localStorage.getItem('AllBook');
    allBooks= JSON.parse(mybook);
    if(this.IsalreadyExist()==true)
    {
        index=this.getbookindex();
        allBooks[index].quantity=Number(allBooks[index].quantity)+Number(this.quantity);
        var mybook = JSON.stringify(allBooks);
        localStorage.setItem('AllBook', mybook);
    }
    else
    {
        book=new Books(this.isbn,this.btitle,this.author,this.edition,this.price,this.quantity);
        allBooks.push(book);
        alert(this.btitle+this.author)
        var mybook = JSON.stringify(allBooks);
        localStorage.setItem('AllBook', mybook);
    }
    alert("Operation Successful");
};
// Read Data for Addbook from HTML Form validate it and call addBook for Further processing
function read_addbook_form()
{
    var book_id="#add input[type]";
    if(validateForm(book_id)==false)
        return 0;
    if (validateParameter(temp)==false)
    {
        //alert("Book Data is not available to add");
        return;
    }
    book=new Books(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5]);
    book.addbook()
}
 // Validate Form Fields lengths and types
function validateForm(id)
{
    temp=[];
    var elements = document.querySelectorAll(id);
    if (validateParameter(elements)==false)
    {
        alert("No Form Data Available to Validate");
        return;
    }
    for (var i = 0,element; element = elements[i++];)
    {
        temp[i-1]=element.value;
        if (element.type == "text" || element.type=="password")
        {
            if(typeof element.value==="string")
            {
                len=element.value.length;
                if(!(len>0 && len<30))
                {
                    alert("Enter " +  element.name +" within length 1 to 30" );
                    return false;
                }
            }
            else
            {
                alert("Enter "+  element.name+" of String type" );
                return false;
            }
         }
        if(element.type=="number")
        {
            len=element.value.length;
            if(element.name=="cardno")
            {
                if(len!=6)
                {
                    alert("Enter " +  element.name +" of length 6" );
                    return false;
                }
            }
            if(!(len>0 && len<20))
            {
                 alert("Enter " +  element.name +" within length 1 to 10" );
                 return false;
            }
        }
        if(element.type=="email")
        {
            var filter= /^([a-zA-Z0-9_.-])+@(([a-zA-Z0-9-])+.)+([a-zA-Z0-9]{2,4})+$/;
            if (!filter.test(element.value))
            {
                alert('Please enter a valid e-mail address.');
                return false;
            }
        }
    }
    return true;
}
/* Shows all Books Available to BUY */
function ShowBook(book)
{
    if (validateParameter(book)==false)
    {
        return;
    }
    var div1 = document.createElement('div');
    div1.style.float="left";
    div1.style.margin="20px";
    div1.style.border="2px solid black";
    div1.style.padding="20px";
    div1.innerHTML="Title: "+book.btitle+" <br> Author: "+book.author+"<br>Edition: "+book.edition+ " <br>Price: "+ book.price+ "<br>Availability: "+book.quantity+ "Copies <br> ";
    var btn=document.createElement("BUTTON");
    btn.innerText="Buy Book";
    btn.id=book.btitle;
    btn.className=book.author;
    btn.onclick=Buybook_onclick;
    div1.appendChild(btn);
    document.body.appendChild(div1);
}
/* this function is called when a user fills the Search book form
and enter button. This function calls SearchBook function for Further
Processing */
function SearchBook_onclick()
{
    var is_book;
    var search_id="#search input[type]";
    if(validateForm(search_id)==false)
        return false;
    if (validateParameter(temp)==false)
    {
        return;
    }
    is_book=SearchBook(temp[0],temp[1]);
    var book = new Books(0,temp[0],temp[1],0,0,0);
    if(is_book==true)
    {
        book_index=book.getbookindex();
        ShowBook(allBooks[book_index]);
    }
    else
    {
        alert("Book is not available");
        showall();
    }
}
/*Make Search by entering Book Title and Author Name
if Book available shows that book detail.*/
function SearchBook(book_title,book_author)
{
    var mybook=localStorage.getItem('AllBook');
    if (validateParameter(mybook)==false)
    {
        alert("Books not available");
        return;
    }
    for(var i=0;i<allBooks.length;i++)
    {
        if(allBooks[i].btitle==book_title&&allBooks[i].author==book_author)
        {
            return true;
        }
    }
    return false;
}
 //Show All available Books
function showall()
{
    var mybook=localStorage.getItem('AllBook');
    if (validateParameter(mybook)==false)
    {
        alert("Books not available");
        return;
    }
    allBooks= JSON.parse(mybook);
    for(var i=0;i<allBooks.length;i++)
    {
        ShowBook(allBooks[i]);
    }
}
 // Checks if user alredy exist
User.prototype.IsUseralreadyExist=function()
{
    var myuser=localStorage.getItem('AllUser');
    if (validateParameter(myuser)==false)
    {
        alert("No Users Data found");
        return;
    }
    allUsers= JSON.parse(myuser);
    for(var i=0;i<allUsers.length;i++)
    {
        if(allUsers[i].username==this.username&&allUsers[i].userpassword==this.userpassword)
        {
            return true;
        }
    }
    return false;
};
// This method adds new user to storage if not such user already exist
User.prototype.adduser=function()
{
    var myuser=localStorage.getItem('AllUser');
    if (validateParameter(myuser)==false)
    {
        return;
    }
    allUsers= JSON.parse(myuser);
    if(this.IsUseralreadyExist()==false)
    {
        user=new User(this.userid,this.username,this.userpassword,this.email,this.cardno,this.amount);
        allUsers.push(user);
        var myuser = JSON.stringify(allUsers);
        localStorage.setItem('AllUser', myuser);
        alert("Operation Successful");
        return true;
    }
    return false;
};
 /* when user click signup button it validates all signup form fields
 call add user method of User Prototype to add given user in storage */
function adduser_onclick()
{
    var signup_id="#signup input[type]";
    if(validateForm(signup_id)==false){
        return false;
    }
    if (validateParameter(temp)==false)
    {
        alert("No User Data Available");
        return;
    }
    current_user=new User(allUsers.length+1,temp[0],temp[1],temp[2],temp[3],temp[4]);
    var user_status;
    user_status=current_user.adduser();
    if(user_status)
    {
        window.location= 'Login.html';
    }
    else
    {
        alert("Try different User name. This User already exist");
    }
}
// Show all users
function showallusers()
{
    var user_p_id=document.getElementById("showuser");
    if (validateParameter(user_p_id)==false)
    {
        alert("User could not be shown");
        return;
    }
    user_p_id.innerHTML="";
    for(var i=0;i<allUsers.length;i++)
    {
        Showuser(allUsers[i],user_p_id);
    }
}
 // Show a single user
function Showuser(user1,user_p_id)
{
    user_p_id.innerHTML= user_p_id.innerHTML+ "<div style='float: left;padding: 20px; border: 2px solid black;margin: 30px;'>Username: "+user1.username+" <br> Userpassword: "+user1.userpassword+"<br>Email: "+user1.email+ " <br>Card No: "+ user1.cardno+ "<br>Available Amount: "+user1.amount+ "<br> </div>";
}
// Gets User by giving Username
User.prototype.getuser=function ()
{
    var myuser=localStorage.getItem('AllUser');
    if (validateParameter(myuser)==false)
    {
        return;
    }
    allUsers= JSON.parse(myuser);
    for(var i=0;i<allUsers.length;i++)
    {
        if(allUsers[i].username==this.username)
        {
            return i;
        }
    }
    return -1;
    //return false;
}
// Login User
User.prototype.loginuser=function()
{
    if(this.IsUseralreadyExist())
    {
        //var getInput = document.getElementById("name").value;
        //alert(this.username);
        localStorage.setItem("UserNames",this.username);
        return true;
    }
    else
    return false
}
/* This function is called when user enter his username and password in HTML login Form
and Submit it. It calls Login method of User Prototype for further Processing. */
function loginuser_onclick()
{
    var login_id="#login input[type]";
    if(validateForm(login_id)==false){
        return false;
    }
    if (validateParameter(temp)==false)
    {
        return;
    }
    current_user=new User("",temp[0],temp[1],"","","");
    if(current_user.loginuser())
    {
        window.location= 'SearchBook.htm';
        return true;
    }
    else
    {
        alert("No Such User exist");
        return false;
    }
}
// This Shows Details of Currently Online User
function viewprofile()
{
    var profile=document.getElementById("viewpro");
    if (validateParameter(profile)==false)
    {
        return false;
    }
    profile.innerText="";
    current_user=new User(0,localStorage.getItem("UserNames"),"","",0,0);
    var usertemp=current_user.getuser();
    if (validateParameter(usertemp)==false)
    {
        return false;
    }
    Showuser(allUsers[usertemp],profile);
    return true;
}


/* when a user click Buy Book button this function gets user and book index and
calls Buy Book function to ensure Buy Book operation
*/
function Buybook_onclick()
{
    var mybook=localStorage.getItem('AllBook');
    allBooks= JSON.parse(mybook);
    var myuser=localStorage.getItem('AllUser');
    if (validateParameter(myuser)==false)
    {
        return;
    }
    allUsers= JSON.parse(myuser);
    console.log(this.id+" "+this.className);
    var book = new Books(0,this.id,this.className,0,0,0);
    var book_index=book.getbookindex();
    if(book_index==-1)
        return false;
    console.log(book_index);
    current_user=new User(0,localStorage.getItem("UserNames"),"","",0,0);
    var user_index=current_user.getuser();
    if (validateParameter(user_index)==false)
    {
        return;
    }
    console.log(allUsers[user_index].amount);
    if(BuyBook(book_index,user_index))
    {
        window.location='showallbooks.html';
    }

}
/* Buy Book takes Book index and user index as input and modify user amount and Book
quantity in order to keep track of available books */
function BuyBook(book_index,user_index)
{
    // validate books and user storage
    var mybook=localStorage.getItem('AllBook');
    var myuser=localStorage.getItem('AllUser');
    if (validateParameter(myuser)==false || validateParameter(mybook)==false)
    {
        return;
    }
    allBooks= JSON.parse(mybook);
    allUsers= JSON.parse(myuser);
    // checks if enough amount available to buy book & and also Copies of Bookk available
    if(Number(allUsers[user_index].amount)>Number(allBooks[book_index].price)&&Number(allBooks[book_index].quantity)>0)
    {
        allUsers[user_index].amount=Number(allUsers[user_index].amount)-Number(allBooks[book_index].price);
        allBooks[book_index].quantity=Number(allBooks[book_index].quantity)-1;
        // Modify Storage to keep Track of new Record
        var myuser = JSON.stringify(allUsers);
        localStorage.setItem('AllUser', myuser);
        var mybook = JSON.stringify(allBooks);
        localStorage.setItem('AllBook', mybook);
        alert("Operation Successful");
        return true;
    }
    else
    {
        alert("Check availability of Book  or Amount to ensure Buy");
        return false;
    }
}


