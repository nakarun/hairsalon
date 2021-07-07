<template>
  <div class="posts">
    <v-card>
      <v-card-title>お知らせ投稿一覧</v-card-title>
      <v-data-table
        :headers="headers"
        :items="formattedPosts"
        class="elevation-0"
      >
        <template v-slot:item.edit="{ item }">
          <v-icon
            small
            class="mr-2"
            @click="editItem(item)"
          >
            mdi-pencil
          </v-icon>
        </template>
        <template v-slot:item.delete="{ item }">
          <v-icon
            small
            @click="deleteItem(item)"
          >
            mdi-delete
          </v-icon>
        </template>
      </v-data-table>
    </v-card>
  </div>
</template>

<script>
import api from "@/services/api";
import datetimeFormat from "@/services/datetimeFormat";


export default {
  name: "Posts",
  computed: {
    formattedPosts() {
      const formattedPosts = [];
      this.posts.forEach(post => {
        formattedPosts.push({
          id: post.id,
          title: post.title,
          published: datetimeFormat(post.published, 'YYYY年MM月DD日'),
          edit: 'edit',
          delete: 'delete',
        })
      })
      return formattedPosts;
    },
  },
  data: () => ({
    headers: [
      {
        text: '投稿日時',
        align: 'start',
        sortable: false,
        value: 'published'
      },
      { text: '投稿タイトル', value: 'title' },
      { text: '編集', value: 'edit' },
      { text: '削除', value: 'delete' },
    ],
    posts: [],
  }),
  methods: {
    fetchItems() {
      this.posts = [];
      api.get('/news/')
      .then(response => {
        this.posts = response.data;
      })
      .catch(function(error) {
        console.log(error);
      })
    },
    editItem(item) {
      console.log(item)
    },
    deleteItem(item) {
      console.log(item);
      api.delete(`/news/${item.id}/`)
      .then(() => {
        this.fetchItems();
      })
      .catch(function(error) {
        console.log(error);
      })
    },
  },
  created: function() {
    this.fetchItems();
  }
}
</script>

<style scoped>
.posts {
  padding: 10px;
}
</style>