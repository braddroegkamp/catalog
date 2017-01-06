from flask import Blueprint, render_template, request, redirect, url_for, flash
from database_setup import User, Category, Item
from item_catalog import session
from login_detail import getStateToken, login_session

app_main = Blueprint('app_main', __name__)


# Main Page - Show Catalog
@app_main.route('/')
@app_main.route('/catalog/')
def showCatalog():
	categories = session.query(Category).order_by(Category.name.asc())
	items = session.query(Item).order_by(Item.last_time.desc()).limit(6)
	logged_in = 'username' in login_session
	return render_template('mainPage.html',
	                       categories=categories,
	                       items=items,
	                       logged_in=logged_in,
	                       STATE=getStateToken())


# Category Page - Show Items in Category
@app_main.route('/catalog/<string:category_name>/')
@app_main.route('/catalog/<string:category_name>/items')
def showCategory(category_name):
	categories = session.query(Category).order_by(Category.name.asc())
	category_id = session.query(Category).filter_by(name=category_name).one().id
	items = session.query(Item).filter_by(category_id=category_id).all()
	return render_template('categoryPage.html',
                           category_name=category_name,
                           categories=categories,
                           items=items,
						   STATE=getStateToken())


# Item Page - Show Details of Item
@app_main.route('/catalog/<string:category_name>/<string:item_name>')
def showItem(category_name, item_name):
	item = session.query(Item).filter_by(name=item_name).one()
	logged_in = 'username' in login_session
	return render_template('itemPage.html',
	                       item=item,
	                       logged_in=logged_in,
	                       STATE=getStateToken())


# New Item Page - Enter new Item
@app_main.route('/catalog/new', methods=['GET', 'POST'])
def newItem():
	if 'username' not in login_session:
		flash('Please log in to create new items')
		return redirect('/catalog/')
	if request.method == 'POST':
		category_id = session.query(Category).filter_by(name=request.form['category']).one().id
		newItem = Item(name=request.form['name'],
		               description=request.form['description'],
		               category_id=category_id,
					   user_id=login_session['user_id'])
		session.add(newItem)
		session.commit()
		flash('%s Successfully Created' % newItem.name)
		return redirect(url_for('.showCategory',
		                        category_name=request.form['category'],
		                        STATE=getStateToken()))
	else:
		return render_template('newItem.html', STATE=getStateToken())


# Edit Item Page - Edit existing Item
@app_main.route('/catalog/<string:category_name>/<string:item_name>/edit', methods=['GET', 'POST'])
def editItem(category_name, item_name):
	if 'username' not in login_session:
		flash('Please log in to edit items')
		return redirect('/catalog/')
	item = session.query(Item).filter_by(name=item_name).one()
	if item.user_id != login_session['user_id']:
		flash('You are not authorized to edit this item.  You are not the author.')
		return redirect(url_for('.showItem', category_name=category_name, item_name=item_name))
	if request.method == 'POST':
		if request.form['name']:
			item.name = request.form['name']
		if request.form['description']:
			item.description = request.form['description']
		if request.form['category']:
			category_id = session.query(Category).filter_by(name=request.form['category']).one().id
			item.category_id = category_id
		session.add(item)
		session.commit()
		flash('%s Successfully Edited' % item.name)
		return redirect(url_for('.showItem',
		                        category_name=request.form['category'],
		                        item_name=item.name,
		                        STATE=getStateToken()))
	else:
		return render_template('editItem.html', item=item, STATE=getStateToken())


# Delete Item Page - Delete existing item
@app_main.route('/catalog/<string:category_name>/<string:item_name>/delete', methods=['GET', 'POST'])
def deleteItem(category_name, item_name):
	if 'username' not in login_session:
		flash('Please log in to delete items')
		return redirect('/catalog/')
	item = session.query(Item).filter_by(name=item_name).one()
	if item.user_id != login_session['user_id']:
		flash('You are not authorized to delete this item.  You are not the author.')
		return redirect(url_for('.showItem', category_name=category_name, item_name=item_name))
	if request.method == 'POST':
		session.delete(item)
		session.commit()
		flash('%s Successfully Deleted' % item.name)
		return redirect(url_for('.showCategory', category_name=category_name, STATE=getStateToken()))
	else:
		return render_template('deleteItem.html', item=item, STATE=getStateToken())