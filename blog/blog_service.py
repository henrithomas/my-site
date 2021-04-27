from .models import Post


class BlogService:
    """
    A database service to handle queries for the blog post models.
    """
    @staticmethod
    def get_single_post(slug):
        """
        This method fetches a single post, using the post id, from the database.

        :param slug: The URL slug for the post
        :param post_id: The id of the post in the database, defaults to 0
        :return: A dictionary containing the single post and title of the web page
        """
        post = Post.objects.filter(slug=slug).only('author', 'date_posted', 'title', 'content').get()

        data = {
            'post': post,
            'title': post.title
        }
        return data

