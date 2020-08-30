import datetime
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from blog.models import CV, Blog

from .views import home_page

class IndexTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
            found = resolve('/')
            self.assertEqual(found.func, home_page)
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<html>', html)
        self.assertIn('<title>Matt R-J\'s CV and Blog</title>', html)
        self.assertTrue(html.endswith('</html>'))

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/index.html')

class PostTest(TestCase):
    def test_does_cv_list_show(self):
        response = self.client.get('/cv')
        self.assertTemplateUsed(response, 'blog/cv_list.html')

    def test_does_blog_list_show(self):
        response = self.client.get('/blog')
        self.assertTemplateUsed(response, 'blog/blog_list.html')

    def test_cv_tag_check(self):
        response = self.client.get('/cv')
        html = response.content.decode('utf8')
        self.assertIn('Achievements', html)
        self.assertIn('Education', html)
        self.assertIn('Work Experience', html)

    def test_can_save_a_CV_POST_request(self):
            # Post.objects.create()
            self.client.post('/cv/new/', data={'tag':'Education', 'title':'testCV1','text':'testCV2', 'start_date': '2020-08-28', 'end_date': '2020-08-29' })
            self.assertEqual(CV.objects.count(), 1)
            new_item = CV.objects.first()
            self.assertEqual(new_item.tag, 'Education')
            self.assertEqual(new_item.title, 'testCV1')
            self.assertEqual(new_item.text, 'testCV2')
            self.assertEqual(new_item.start_date,  datetime.date(2020, 8, 28))
            self.assertEqual(new_item.end_date, datetime.date(2020, 8, 29))

    def test_redirects_after_CV_POST(self):
        response = self.client.post('/cv/new/', data={'tag': 'Education', 'title': 'testCV1', 'text': 'testCV2',
                                             'start_date': '2020-08-28', 'end_date': '2020-08-29'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv/1/')

    def test_displays_all_CV_posts(self):
        response = self.client.post('/cv/new/', data={'tag': 'Education', 'title': 'testCV1', 'text': 'testCV2',
                                                        'start_date': '2020-08-28', 'end_date': '2020-08-29'})
        response = self.client.post('/cv/new/', data={'tag': 'Work Experience', 'title': 'anotherTestCV1', 'text': 'anotherTestCV2',
                                                        'start_date': '2020-08-28', 'end_date': '2020-08-29'})
        # Item.objects.create(text='itemey 2')

        response = self.client.get('/cv')

        self.assertIn('testCV1', response.content.decode())
        self.assertIn('anotherTestCV1', response.content.decode())

    def test_only_saves_CV_posts_when_necessary(self):
        self.client.get('/cv')
        self.assertEqual(CV.objects.count(), 0)

    def test_can_save_a_blog_POST_request(self):
        # Post.objects.create()
        self.client.post('/blog/new/', data={'title': 'testBlog1', 'text': 'testBlog2'})
        self.assertEqual(Blog.objects.count(), 1)
        new_item = Blog.objects.first()
        self.assertEqual(new_item.title, 'testBlog1')
        self.assertEqual(new_item.text, 'testBlog2')


    def test_redirects_after_blog_POST(self):
        response = self.client.post('/blog/new/', data={ 'title': 'testBlog1', 'text': 'testBlog2'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/blog/1/')

    def test_displays_all_CV_posts(self):
        response = self.client.post('/blog/new/', data={ 'title': 'testBlog1', 'text': 'testBlog2'})
        response = self.client.post('/blog/new/', data={ 'title': 'anotherTestBlog1', 'text': 'anotherTestBlog2'})
        # Item.objects.create(text='itemey 2')

        response = self.client.get('/blog')

        self.assertIn('testBlog1', response.content.decode())
        self.assertIn('anotherTestBlog1', response.content.decode())

    def test_only_saves_CV_posts_when_necessary(self):
        self.client.get('/blog')
        self.assertEqual(Blog.objects.count(), 0)


