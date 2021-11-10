from flask import Flask, render_template, url_for, flash, redirect
from city.forms import TopCities
from city import app

top_cities = ["Paris", "London", "Rome", "Tahiti"]
title = 'Top Cities'
name = 'Steven Chen'  

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = TopCities()
    if form.validate_on_submit():
        flash(f'Submitted for {form.city_name.data}!',
              category='success')
        top_cities.insert(form.city_rank.data-1,form.city_name.data)
        return redirect('home')
    return render_template("home.html",title=title,name=name,
                           top_cities=top_cities,form=form)