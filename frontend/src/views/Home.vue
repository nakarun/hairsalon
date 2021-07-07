<template>
  <div class="home">
    <Stamp />
    <Pointcards ref="pointcards"/>
    <CreatePointcard @created="fetchPointcards"/>
    <Posts ref="posts"/>
    <Post @posted="fetchPosts"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Stamp from "@/components/Stamp"
import Pointcards from "@/components/Pointcards"
import CreatePointcard from "@/components/CreatePointcard";
import Posts from "@/components/Posts"
import Post from "@/components/Post"

export default {
  name: "Home",
  components: {
    Stamp,
    Pointcards,
    CreatePointcard,
    Posts,
    Post
  },
  methods: {
    fetchPointcards() {
      console.log(this.$store.state.salon.uuid);
      this.$store.dispatch("pointcards/getPointcards", {
        salon: this.$store.state.salon.uuid,
      })
      .then(() => {
        console.log('get salon data ad pointcards.');
      })
    },
    fetchPosts() {
      this.$refs.posts.fetchItems();
    }
  },
  created: function () {
    // staff.uuidからsalon情報を取得
    this.$store.dispatch("salon/getSalonData", {
      staff: this.$store.state.auth.useruuid,
    })
    .then(() => {
      // salonに紐づくポイントカードを取得
      this.fetchPointcards();
    })
  },
};
</script>
