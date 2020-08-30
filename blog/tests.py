import datetime
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from blog.models import CV

from .views import home_page

class IndexTest(TestCase):
    pass
#     def test_root_url_resolves_to_home_page_view(self):
#             found = resolve('/')
#             self.assertEqual(found.func, home_page)
#     def test_home_page_returns_correct_html(self):
#         request = HttpRequest()
#         response = home_page(request)
#         html = response.content.decode('utf8')
#         self.assertIn('<html>', html)
#         self.assertIn('<title>Matt R-J\'s CV</title>', html)
#         self.assertTrue(html.endswith('</html>'))
#
#     def test_uses_home_template(self):
#         response = self.client.get('/')
#         self.assertTemplateUsed(response, 'blog/index.html')
#
# class PostTest(TestCase):
#     def test_can_does_postlist_show(self):
#         response = self.client.get('/post')
#         self.assertTemplateUsed(response, 'blog/cv_list.html')
#
#     def test_post_tag_check(self):
#         response = self.client.get('/post')
#         html = response.content.decode('utf8')
#         self.assertIn('Achievements', html)
#         self.assertIn('Education', html)
#         self.assertIn('Work Experience', html)
#
#     def test_can_save_a_POST_request(self):
#             # Post.objects.create()
#             self.client.post('/post/new/', data={'tag':'Education', 'title':'testPost1','text':'testPost2', 'start_date': '2020-08-28', 'end_date': '2020-08-29' })
#             self.assertEqual(Post.objects.count(), 1)
#             new_item = Post.objects.first()
#             self.assertEqual(new_item.tag, 'Education')
#             self.assertEqual(new_item.title, 'testPost1')
#             self.assertEqual(new_item.text, 'testPost2')
#             self.assertEqual(new_item.start_date,  datetime.date(2020, 8, 28))
#             self.assertEqual(new_item.end_date, datetime.date(2020, 8, 29))
#
#     def test_redirects_after_POST(self):
#         response = self.client.post('/post/new/', data={'tag': 'Education', 'title': 'testPost1', 'text': 'testPost2',
#                                              'start_date': '2020-08-28', 'end_date': '2020-08-29'})
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response['location'], '/post/1/')
#
#     def test_displays_all_posts(self):
#         response = self.client.post('/post/new/', data={'tag': 'Education', 'title': 'testPost1', 'text': 'testPost2',
#                                                         'start_date': '2020-08-28', 'end_date': '2020-08-29'})
#         response = self.client.post('/post/new/', data={'tag': 'Work Experience', 'title': 'anotherTestPost1', 'text': 'anotherTestPost2',
#                                                         'start_date': '2020-08-28', 'end_date': '2020-08-29'})
#         # Item.objects.create(text='itemey 2')
#
#         response = self.client.get('/post')
#
#         self.assertIn('testPost1', response.content.decode())
#         self.assertIn('anotherTestPost1', response.content.decode())
#
#     def test_only_saves_posts_when_necessary(self):
#         self.client.get('/post')
#         self.assertEqual(Post.objects.count(), 0)

