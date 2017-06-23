describe("BookStore", function() {
  var book;
  var user;

  beforeEach(function() {
    book = new Books(15,"DS","abc",2,50,1);
    user = new User(8,"Fariha",456,"fariha@gmail.com",789234,5000);
  });
  it("should be able validate parameters", function() {
    var input_para;
    result_validate=validateParameter(input_para);
    expect(false).toEqual(result_validate);
  });
  it("should be able to get Book index", function() {
    book = new Books(15,"DS","abc",2,50,1);
    index=book.getbookindex();
    expect(1).toEqual(index);
  });
  it("User should be able to check Available Copies of book", function() {
    index=book.getbookindex();
    if(validateParameter(allBooks)&&index!=false)
    {
      original_quantity=allBooks[index].quantity;
      quantity_byfun=book.getbookquantity();
      expect(original_quantity).toEqual(quantity_byfun);
    }
  });
  it("User should be able to Search Book By Title and Author Name of Book ", function() {
    var search_result;
    search_result=SearchBook("DS","abc");
    expect(search_result).toEqual(true);
    search_result=SearchBook("islamiyat","hazrat");
    expect(search_result).toEqual(false);
  });
  it("User should be able to add book", function() {
    var existing_quantity=0;
    if(book.IsalreadyExist())
    {
      //alert("Book already exist");
      existing_quantity=book.getbookquantity();
    }
    else
    {
        //alert("Book not exist");
    }
    existing_quantity+=1;
    book.addbook();
    new_quantity=book.getbookquantity();
    //alert(book.getbookindex());
    expect(existing_quantity).toEqual(new_quantity);
  });
  it("User should be able to buy Book", function() {
    var mybook=localStorage.getItem('AllBook');
    var myuser=localStorage.getItem('AllUser');
    if (validateParameter(myuser)==false || validateParameter(mybook)==false)
    {
        return;
    }
    allBooks= JSON.parse(mybook);
    allUsers= JSON.parse(myuser);
    var user_index=1;
    var book_index=6;
    previous_amount=Number(allUsers[user_index].amount);
    previous_quantity=Number(allBooks[book_index].quantity);
    BuyBook(book_index,user_index);
    if(previous_amount>Number(allBooks[book_index].price)&&previous_quantity>0)
    {
      expect(Number(allUsers[user_index].amount)).toEqual(previous_amount-Number(allBooks[book_index].price));
      expect(Number(allBooks[book_index].quantity)).toEqual(previous_quantity-1);
    }
    else
    {
      expect(Number(allUsers[user_index].amount)).toEqual(previous_amount);
      expect(Number(allBooks[book_index].quantity)).toEqual(previous_quantity);
    }

  });
  it("Should be able to get Current User", function() {
    user = new User(0,"huma",0,"",0,0);
    user_index=user.getuser();
    //alert("User_index "+user_index);
    var myuser=localStorage.getItem('AllUser');
    allUsers= JSON.parse(myuser);
    if(user_index!=-1)
    {
      expect(allUsers[user_index].username).toEqual("huma");
    }
  });
  it("User should be able to SignUp", function() {
    var myuser=localStorage.getItem('AllUser');
    if (validateParameter(myuser)==false)
    {
        return;
    }
    allUsers= JSON.parse(myuser);
    index=allUsers.length;
    status_result=user.IsUseralreadyExist();
    user.adduser();
    if(status_result==false)
    {
      myuser=localStorage.getItem('AllUser');
      allUsers= JSON.parse(myuser);
      expect(allUsers[index].username).toEqual(user.username);
    }
    else
    {
      myuser=localStorage.getItem('AllUser');
      allUsers= JSON.parse(myuser);
      expect(validateParameter(allUsers[index])).toEqual(false);
    }

  });
  it("User should be able to Login", function() {
  user = new User(0,"huma",123,"",0,0);
  expect(user.loginuser()).toEqual(true);
  user = new User(0,"huma",456,"",0,0);
  expect(user.loginuser()).toEqual(false);
  });
  it("Should be able to Check User already exist", function() {
  user = new User(0,"huma",123,"",0,0);
  expect(user.IsUseralreadyExist()).toEqual(true);
  user = new User(0,"huma",456,"",0,0);
  expect(user.IsUseralreadyExist()).toEqual(false);
  user = new User(0,"no user",456,"",0,0);
  expect(user.IsUseralreadyExist()).toEqual(false);
  });


});
