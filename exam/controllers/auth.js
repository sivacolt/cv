const mysql = require("mysql");

const db = mysql.createConnection({
    host:process.env.DATABASE_HOST,
    user: process.env.DATABASE_USER,
    password: process.env.DATABASE_PASSWORD,
    database: process.env.DATABASE

});


exports.register = (req,res) => {
    console.log(req.body);
    
    const{ name, email, password} =req.body;

    db.query('SELECT email FROM users WHERE email =?',[email],(error,results) =>{
        if(error){
            console.log(error);
        }
        if(results.length > 0){
            return res.render('register',{
                message:'that email in use'
            });
        } 
        
        db.query('INSERT INTO users SET ?',{name:name, email:email,password:password},(error,results)=>{
            if(error){
                console.log(error);
            }
            else{
                console.log(results)
                return res.render('register',{
                    message:'user registered'
                })
            }
        })

    });

    res.send("form submitted");
}