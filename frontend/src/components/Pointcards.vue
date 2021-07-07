<template>
  <div class="pointcards">
    <v-card class="pb-1">
      <v-card-title>作成したポイントカード</v-card-title>
      <v-card class="ma-5 pa-3"
              v-for="pointcard in pointcards"
              :key="pointcard.uuid"
              outlined
      >
        <v-card-subtitle class="text-sm-left">Name: 〇〇 〇〇様</v-card-subtitle>
        <hr>
        <div class="frames">
          <table class="table table-bordered">
            <tr v-for="vindex in pointcard.vertical_cells_count"
                :key="vindex"
                class="frame-line"
            >
              <td v-for="hindex in pointcard.horizontal_cells_count"
                  :key="hindex"
              ></td>
            </tr>
          </table>
        </div>
        <hr>
        <v-card-text class="text-sm-caption text-sm-left">ご来店１回につき、１枠捺印致します。（お会計金額2,000円以上）</v-card-text>
      </v-card>
    </v-card>
  </div>
</template>

<script>

export default {
  name: "Pointcards",
  data: () => ({
  }),
  computed: {
    pointcards: function () {
      return this.$store.state.pointcards.pointcards;
    }
  },
  methods: {
  },
  created: function() {
  },
}
</script>

<style scoped>
.pointcards {
  padding: 10px;
}

div.frames {
  margin: 16px;
}

tr.frame-line {
  height: 4em;
}
</style>