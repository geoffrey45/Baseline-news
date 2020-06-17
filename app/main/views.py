from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_headlines,get_everything,search_news

@main.route('/')
def index():
	everything = get_everything()
	title = 'News Highlight'
	searching_news = request.args.get('keyword')

	if searching_news:
		redirect(url_for('.search',keyword = searching_news))
	return render_template('index.html',title = title,everything = everything)

@main.route('/source/<source>')
def Headlines(source):
	sources = get_sources()
	Headlines = get_headlines(source)
	print(Headlines)

	return render_template('headlines.html',sources = sources,Headlines = Headlines)

@main.route('/sources')
def sources():
	sources = get_sources()
	print(sources)
	return render_template('sources.html',sources = sources)

@main.route('/search/<keyword>')
def search(keyword):
	keyword_list = keyword.split(" ")
	keyword_format = '%20'.join(keyword_list)
	searched_news = search_news(keyword_format)
	title = f'Search results for {keyword} '
	return render_template('search.html',searched_news = searched_news)