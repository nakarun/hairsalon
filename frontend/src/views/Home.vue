<template>
  <div class="home">
    <Pointcards ref="pointcards"/>
    <CreatePointcard @created="fetchPointcards()"/>
    <Posts ref="posts"/>
    <Post @posted="fetchPosts"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Pointcards from "@/components/Pointcards"
import CreatePointcard from "@/components/CreatePointcard";
import Posts from "@/components/Posts"
import Post from "@/components/Post"

export default {
  name: "Home",
  components: {
    Pointcards,
    CreatePointcard,
    Posts,
    Post
  },
  methods: {
    fetchPointcards() {
      this.$refs.pointcards.fetchItems();
    },
    fetchPosts() {
      this.$refs.posts.fetchItems();
    }
  }
};
</script>
