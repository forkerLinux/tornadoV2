
function getCookie(name){
       var result = null;
          //对cookie信息进行相应的处理，方便搜索
          var myCookie = ""+document.cookie+";"; 
            var searchName = ""+name+"=";
             var startOfCookie = myCookie.indexOf(searchName);
              var endOfCookie;
              if(startOfCookie != -1){
              startOfCookie += searchName.length;
              endOfCookie = myCookie.indexOf(";",startOfCookie);
              result = (myCookie.substring(startOfCookie,endOfCookie));
            }
    return result;
} //end function
 
