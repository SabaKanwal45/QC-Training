 //Book Objects Prototyp/window.onload = alert(localStorage.getItem("UserNames"));
 function Books(isbn, title, author, edition, price, quantity)
 {
     this.isbn = isbn;
     this.btitle = title;
     this.author = author;
     this.edition = edition;
     this.price = price;
     this.quantity = quantity;
 }
 //Some books initially in Storage
 var allBooks = [];
 var book = new Books(1,"oop","abc",2,200,5);
 allBooks.push(book);
 book = new Books(1,"DS","abc",2,100,5);
 allBooks.push(book);
 book = new Books(1,"SE","abc",2,150,5);
 allBooks.push(book);
 book = new Books(1,"programming","xyz",2,250,5);
 allBooks.push(book);
 book = new Books(1,"english","amjad",2,220,5);
 allBooks.push(book);
 book = new Books(1,"","abc",2,250,5);
 allBooks.push(book);
 var temp=[];
 var val=0;
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
 //Some User initially in Storage
 var allUsers = [];
 var user1= new User(1,"huma",123,"abc@gmail.com",213456,1000);
 allUsers.push(user1);
 user1 = new User(2,"maleeha",456,"cde@gmail.com",215367,500);
 allUsers.push(user1);
 user1 = new User(3,"fazila",678,"fgh@gmail.com",317685,2000);
 allUsers.push(user1);
 user1 = new User(4,"muzna",910,"ijk@gmail.com",245987,5000);
 allUsers.push(user1);
 user1 = new User(5,"munaza",112,"lmn@gmail.com",287956,7000);
 allUsers.push(user1);
 user1= new User(6,"komal",115,"opq@gmail.com",267986,5000);
 allUsers.push(user1);
 //Checks if Book already in storage
 function IsalreadyExist(book)
 {
     for(var i=0;i<allBooks.length;i++)
     {
         if(allBooks[i].btitle==book.btitle&&allBooks[i].author==book.author)
         {
             alert("Book already exit");
             allBooks[i].quantity=Number(allBooks[i].quantity)+Number(book.quantity);
             return 0;
         }
     }
     return 1;

 }
 function addBook()
 {
     var id="#add input[type]";
     if(validateForm(id)==false)
         return 0;
     book=new Books(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5]);
     if(IsalreadyExist(book))
     {
         allBooks.push(book);
         console.log(book.btitle);
     }
     alert("Operation Successful");
 }
 // Validate Form and add Books in Storage
 function validateForm(id)
 {
     temp=[];
     var elements = document.querySelectorAll(id);
     for (var i = 0,element; element = elements[i++];)
     {
         //alert(i+" "+element.value);
         temp[i-1]=element.value;
         if (element.value === "")
         {
             alert("Please fill "+ element.name+" Field");
             return false;
         }
     }
     //console.log(temp[0]+" "+temp[1]);
     return true;
 }
 // Show Book Details
 function ShowBook(book,para)
 {
     //var btn=document.createElement('div');
     //para.style.float="left";
     para.innerHTML= para.innerHTML+ "<div style='float: left;margin: 10px'>Title: "+book.btitle+" <br> Author: "+book.author+"<br>Edition: "+book.edition+ " <br>Price: "+ book.price+ "<br>Availability: "+book.quantity+ "Copies <br> <input id='btn'+val type='button' onclick='Buybook(book)' value='Buy Book'> </div>";
     //var btn=document.createElement("BUTTON");
     //btn.id=
 }
 //Make Search by entering Book Title and Author Name
 function SearchBook()
 {
     var is=false;
     var id1="#search input[type]";
     if(validateForm(id1)==false)
         return 0;
     //var para = document.createElement('div');
     //para.style.columnSpan=4;
     var para=document.getElementById("showbook");
     para.innerHTML="";
     val=0;
     for(var i=0;i<allBooks.length;i++)
     {
         if(allBooks[i].btitle==temp[0]&&allBooks[i].author==temp[1])
         {
             //console.log("abc");
             //console.log(temp[0]+" "+temp[1]);
             ShowBook(allBooks[i],para);
             is=true;
             val=val+1;
         }
     }
     if(is==false)
     {
         showall();
     }
 }
 //Show All available Books
 function showall()
 {
     var para=document.getElementById("showbook");
     para.innerHTML="";
     for(var i=0;i<allBooks.length;i++)
     {
         ShowBook(allBooks[i],para);

     }

 }
 // Checks if user alredy exist
 function IsUseralreadyExist(user1)
 {
     for(var i=0;i<allUsers.length;i++)
     {
         if(allUsers[i].username==user1.username&&allUsers[i].userpassword==user1.userpassword)
         {
             alert("User already exit try Different Username");
             return 0;
         }
     }
     return 1;

 }
 // Add new User
 function adduser()
 {
     var id="#signup input[type]";
     if(validateForm(id)==false){
         return 0;
     }
     user1=new User(allUsers.length,temp[0],temp[1],temp[2],temp[3],temp[4]);
     if(IsUseralreadyExist(user1))
     {
         allUsers.push(user1);
         //console.log(book.btitle);
         alert("Operation Successful");
         window.location= 'Login.html';
     }

 }
 // Show all users
 function showallusers()
 {
     var para=document.getElementById("showuser");
     para.innerHTML="";
     for(var i=0;i<allUsers.length;i++)
     {
         Showuser(allUsers[i],para);

     }

 }
 // Show a single user
 function Showuser(user1,para)
 {
     //para.style.float="left";
     para.innerHTML= para.innerHTML+ "<div style='float: left;margin: 10px'>Username: "+user1.username+" <br> Userpassword: "+user1.userpassword+"<br>Email: "+user1.email+ " <br>Card No: "+ user1.cardno+ "<br>Available Amount: "+user1.amount+ "<br> </div>";
 }
 // Login User
 function loginuser()
 {
     var id="#login input[type]";
     if(validateForm(id)==false){
         return 0;
     }
     //console.log(temp[0]+ " "+temp[1]);
     user1=new User("",temp[0],temp[1],"","","");
     if(IsUseralreadyExist(user1)==0)
     {
         var getInput = document.getElementById("na").value;
         localStorage.setItem("UserNames",getInput);
         //console.log(getInput);
         window.location= 'SearchBook.htm';
     }
     else
     {
         alert("No Such User exist");
     }
 }
 function viewprofile()
 {
     var profile=document.getElementById("viewprofile");
     profile.innerHTML="";
     alert(localStorage.getItem("UserNames"));
     usertemp=getuser(localStorage.getItem("UserNames"));
     if(usertemp==0)
         return 0;
     Showuser(usertemp,profile);
 }
 function getuser(name1)
 {
     for(var i=0;i<allUsers.length;i++)
     {
         if(allUsers[i].username==name1)
         {
             return allUsers[i];
         }
     }
     return 0;

 }
 //Get book from Storage
 function getbook(booktitle,bauthor)
 {
     for(var i=0;i<allBooks.length;i++)
     {
         if(allBooks[i].btitle==booktitle&&allBooks[i].author==bauthor)
         {
             return i;
         }
     }
     return -1;

 }
 //Buy Book
 function Buybook(bookw)
 {
     var i=getbook(bookw.btitle,bookw.author);
     if(i==-1)
         return 0;
     usertemp=getuser(localStorage.getItem("UserNames"));
     if(usertemp.amount>allBooks[i].price)
     {
         usertemp.amount=Number(usertemp.amount)-Number(allBooks[i].price);
         allBooks[i].quantity=Number(allBooks[i].quantity)-1;
         alert("Operation Successful");
     }
     else
     {
         alert("Not Enough Amount to Buy a Book");
         return 0;
     }

 }


