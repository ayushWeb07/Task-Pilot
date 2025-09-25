# import packages
from flask import Blueprint, request, url_for, Response, render_template, flash, session, redirect
from app.models import Todo
from app import db

# create the todos blueprint
todos_bp = Blueprint("todos", __name__)


# get all todos -> "/"
@todos_bp.route("/")
def get_all_todos():
    
    # user is not logged in
    if "username" not in session:
        flash("You must be logged in!", "error")
        return redirect(url_for("auth.login"))
    
    else:
        
        
        todos = (
            Todo.query
            .filter_by(user_id=session["id"])
            .order_by(Todo.is_completed.asc(), Todo.created_at.desc())
            .all()
        )

                
        return render_template("home.html",  todos= todos)
    
    

        
# about -> "/about"
@todos_bp.route("/about")
def show_about():
    
    # user is not logged in
    if "username" not in session:
        flash("You must be logged in!", "error")
        return redirect(url_for("auth.login"))
    
    return render_template("about.html")
        
        


# add todo -> "/add"
@todos_bp.route("/add", methods= ["POST"])
def add_todo():
    
    # user is not logged in
    if "username" not in session :
        flash("You must be logged in!", "error")
        return redirect(url_for("auth.login"))
    
    else:
        
        # get the todo details
        content= request.form.get("content")
        priority= request.form.get("priority")
        user_id= session["id"]
        
            
        new_todo= Todo(content= content, priority= priority, user_id= user_id)
        db.session.add(new_todo)
        db.session.commit()
        
        
        return redirect(url_for("todos.get_all_todos"))
        

# update todo: update todo details
@todos_bp.route("/update/<int:todo_id>", methods= ["GET", "POST"])
def update_todo(todo_id):
        
    # get the todo
    todo= Todo.query.get(todo_id)
    
    if request.method == "GET" and todo:
        return render_template("edit-todo.html", todo= todo)
    
    elif request.method == "POST" and todo:
        
        if request.form.get("content", None) is not None:
            todo.content= request.form["content"]
            
        if request.form.get("priority", None) is not None:
            todo.priority= request.form["priority"]
            
        if request.form.get("is_completed", None) is not None:
            
            # Convert string to actual boolean
            todo.is_completed = True if request.form["is_completed"] == "True" else False
        
        db.session.commit()
        
        flash("Todo details updated", "success")
            
        
    return redirect(url_for("todos.get_all_todos"))
    
        


# delete todo
@todos_bp.route("/delete/<int:todo_id>", methods= ["POST"])
def delete_todo(todo_id):
    
    # get the todo
    todo= Todo.query.get(todo_id)
    
    if todo:
        
        db.session.delete(todo)
        db.session.commit()
                        
        
    return redirect(url_for("todos.get_all_todos"))


