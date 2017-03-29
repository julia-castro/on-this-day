import os, requests
from datetime import date
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from .forms import DateForm

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
  SECRET_KEY='8bfda0dc4c3a4f9684bd2393375a4dd7',
  WTF_CSRF_ENABLED = False
))

@app.route('/', methods=['GET', 'POST'])
def show_articles():
  form = DateForm()
  data = None

  if request.method == 'POST' and form.validate():
    day = form.date.data.day
    day = str(day).zfill(2) if day < 10 else str(day)
    month = form.date.data.month
    month = str(month).zfill(2) if month < 10 else str(month)
    year = str(form.date.data.year)
    date =  year + month + day

    r = requests.get('https://api.nytimes.com/svc/search/v2/articlesearch.json', params={'api-key': app.config['SECRET_KEY'], 'begin_date': date, 'end_date': date})
    r = r.json()['response']['docs']

    data = {'sections': [], 'articles': []}
    for x in r:
      section_name = 'Misc' if x['section_name'] is None else x['section_name']
      if section_name not in data['sections']:
        data['sections'].append(section_name)

      data['articles'].append({'headline': x['headline'], 'pub_date': x['pub_date'], 'lead_paragraph': x['lead_paragraph'], 'byline': x['byline'], 'section': section_name})
    print(data)

  return render_template('list_articles.html', form=form, data=data)