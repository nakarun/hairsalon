module.exports = {
  pages: {
    index: {
      entry: "src/main.js",
      title: "Salon Admin",
    }
  },
  outputDir: "../static/dist",
  indexPath: "../../templates/index.html",
  publicPath: process.env.NODE_ENV === "production"
    ? "/static/dist/"
    : "/"
}