from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from grocery_app.models import GroceryStore, GroceryItem
from grocery_app.forms import GroceryItemForm, GroceryStoreForm

# Import app and db from events_app package so that we can run app
from grocery_app import app, db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    all_stores = GroceryStore.query.all()
    print(all_stores)
    return render_template('home.html', all_stores=all_stores)

@main.route('/new_store', methods=['GET', 'POST'])
def new_store():
    # TODO: Create a GroceryStoreForm
    form = GroceryStoreForm()
    # TODO: If form was submitted and was valid:
    if form.validate_on_submit():
        # - create a new GroceryStore object and save it to the database,
        new_grocery_store = GroceryStore(
            title=form.title.data,
            address=form.address.data
        )
        db.session.add(new_grocery_store)
        db.session.commit()

    
    # - flash a success message, and
        flash('The new store was successfully created')
    # - redirect the user to the store detail page.
        return redirect(url_for('main.store_detail', store_id=new_grocery_store.id))
    # TODO: Send the form to the template and use it to render the form fields
    return render_template('new_store.html', form=form)

@main.route('/new_item', methods=['GET', 'POST'])
def new_item():
    # TODO: Create a GroceryItemForm
    form = GroceryStoreForm()
    # TODO: If form was submitted and was valid:
    if form.validate_on_submit():
    # - create a new GroceryItem object and save it to the database,
        new_item = GroceryItem(
            name=form.name.data,
            price=form.price.data,
            category=form.category.data,
            photo_url=form.photo_url.data,
            store=form.store.data
        )
        db.session.add(new_item)
        db.session.commit()
    # - flash a success message, and
        flash('New item was created successfully.')
    # - redirect the user to the item detail page.
        return redirect(url_for('main_item.detail', item_id=new_store_item.id))
    # TODO: Send the form to the template and use it to render the form fields
    return render_template('new_item.html', form=form)

@main.route('/store/<store_id>', methods=['GET', 'POST'])
def store_detail(store_id):
    store = GroceryStore.query.get(store_id)
    # TODO: Create a GroceryStoreForm and pass in `obj=store`
    form =  GroceryStoreForm(obj=store)
    # TODO: If form was submitted and was valid:
    if form.validate_on_submit():
    # - update the GroceryStore object 
        store.title = form.title.data
        store.address = form.address.data
    # and save it to the database,
        db.session.add(store)
        db.session.commit()
    # - flash a success message, and
        flash('Store detail successfully created')
    # - redirect the user to the store detail page.
        return redirect(url_for('main.store_detail', store_id=store_id))
    # TODO: Send the form to the template and use it to render the form fields
    store = GroceryStore.query.get(store_id)
    return render_template('store_detail.html', store=store, form=form)

@main.route('/item/<item_id>', methods=['GET', 'POST'])
def item_detail(item_id):
    item = GroceryItem.query.get(item_id)
    # TODO: Create a GroceryItemForm and pass in `obj=item`
    form = GroceryItemForm(obj=item)
    # TODO: If form was submitted and was valid:
    if form.validate_on_submit():
    # - update the GroceryItem object
        item.name = form.name.data
        item.price = form.price.data
        item.category = form.price.data
        item.photo_url = form.photo_url.data
        item.store = form.store.data
    # and save it to the database
        db.session.add(item)
        db.session.commit()
    # - flash a success message, and
    flash('Item successfully updated')
    # - redirect the user to the item detail page.
    return redirect(url_for('main.item_detail', item_id=item.id))
    # TODO: Send the form to the template and use it to render the form fields
    item = GroceryItem.query.get(item_id)
    return render_template('item_detail.html', item=item, form =form)
