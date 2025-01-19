<template>
  <div class="bg-gray-100 min-h-screen p-6">
    <div class="container mx-auto max-w-4xl bg-white p-8 rounded-lg shadow-lg">
      <img
          :src="post.main_image"
          :alt="post.title"
          class="w-full h-96 object-cover rounded-lg mb-6"
      />
      <h1 class="text-4xl font-bold text-gray-800 mb-4">{{ post.title }}</h1>
      <p class="text-gray-600 mb-6">{{ post.description }}</p>
      <div class="flex items-center space-x-6 mb-8">
        <button
            @click="editBlog"
            class="mt-2 bg-blue-500 text-white px-4 py-2 rounded-lg"
        >
          Edit
        </button>
      </div>

      <div>
        <h2 class="text-2xl font-semibold text-gray-800 mb-4">Comments</h2>
        <div v-for="comment in comments" :key="comment.id" class="border-b pb-6 mb-6">
          <p class="font-semibold text-gray-800">{{ comment.user }}</p>
          <p class="text-gray-600 mb-2">{{ comment.text }}</p>

          <div v-for="reply in comment.replies" :key="reply.id" class="ml-6">
            <p class="font-semibold text-gray-800">{{ reply.user }}</p>
            <p class="text-gray-600">{{ reply.text }}</p>
          </div>

          <div class="mt-4">
            <textarea
                v-model="newReply[comment.id]"
                placeholder="Write a reply..."
                class="w-full p-2 border border-gray-300 rounded-lg"
            ></textarea>
            <button
                @click="replyToComment(comment.id)"
                class="mt-2 bg-blue-500 text-white px-4 py-2 rounded-lg"
            >
              Reply
            </button>
          </div>
        </div>

        <div class="mt-6">
          <textarea
              v-model="newComment"
              placeholder="Write a comment..."
              class="w-full p-2 border border-gray-300 rounded-lg"
          ></textarea>
          <button
              @click="addComment"
              class="mt-2 bg-blue-500 text-white px-4 py-2 rounded-lg"
          >
            Add Comment
          </button>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PostDetail",
  data() {
    return {
      post: {
        id: null,
        title: '',
        description: '',
        main_image: '',
        likes: 0,
        dislikes: 0
      },
      comments: [],
      newComment: "",
      newReply: {}
    };
  },
  mounted() {
    const postId = this.$route.params.id;
    this.loadPostData(postId);
    this.loadComments(postId);
  },
  methods: {
    loadPostData(postId) {
      const token = localStorage.getItem("access_token");
      fetch(`http://localhost:8000/blog/blogs/${postId}`, {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      })
          .then(response => response.json())
          .then(data => {
            this.post = data;
          })
          .catch(error => console.error("Error loading post data", error));
    },
    loadComments(postId) {
      const token = localStorage.getItem("access_token");
      fetch(`http://localhost:8000/blog/blogs/${postId}/comments/`, {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      })
          .then(response => response.json())
          .then(data => {
            this.comments = data.map(comment => ({
              ...comment,
              id: comment.id || comment.blog
            }));
          })
          .catch(error => console.error("Error loading comments", error));
    },

    addComment() {
      if (this.newComment.trim()) {
        const newComment = {
          id: this.comments.length + 1,
          user: "Anonymous",
          text: this.newComment,
          replies: []
        };
        this.comments.push(newComment);
        this.newComment = "";
      }
    },
    replyToComment(commentId) {
      const replyText = this.newReply[commentId];
      if (replyText.trim()) {
        const comment = this.comments.find(c => c.id === commentId);
        comment.replies.push({
          id: comment.replies.length + 1,
          user: "Anonymous",
          text: replyText
        });
        this.newReply[commentId] = "";
      }
    },
    editBlog(){
      this.$router.push({ name: 'BlogFormEdit', params: { blogId: this.post.id } });
    }

  }
};
</script>

<style scoped>
</style>
