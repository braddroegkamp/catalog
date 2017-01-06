from flask import Blueprint, jsonify, flash, redirect
from item_catalog import session
from database_setup import Category, Item
from login_detail import login_session

app_json_detail = Blueprint('app_json_detail', __name__)


# JSON APIs to view all Catalog Information
@app_json_detail.route('/catalog/JSON')
def catalogJSON():
	if 'username' not in login_session:
		flash('Please log in to access JSON API rendering')
		return redirect('/catalog/')
	else:
		items = session.query(Item).order_by(Item.category_id.asc()).all()
		return jsonify(Item=[i.serialize for i in items])


# JSON APIs to view defined Category Information
@app_json_detail.route('/catalog/<string:category_name>/JSON')
def catalogCategoryJSON(category_name):
	if 'username' not in login_session:
		flash('Please log in to access JSON API rendering')
		return redirect('/catalog/')
	else:
		category_id = session.query(Category).filter_by(name=category_name).one().id
		items = session.query(Item).filter_by(category_id=category_id).all()
		return jsonify(Item=[i.serialize for i in items])
