<template>
  <div class="home">
    <Pointcards />
    <Posts ref="posts"/>
    <Post @posted="fetchPosts"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Pointcards from "@/components/Pointcards"
import Posts from "@/components/Posts"
import Post from "@/components/Post"

export default {
  name: "Home",
  components: {
    Pointcards,
    Posts,
    Post
  },
  methods: {
    fetchPosts() {
      this.$refs.posts.fetchItems();
    }
  }
};
</script>
