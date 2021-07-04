(function(e){function t(t){for(var s,a,i=t[0],c=t[1],u=t[2],f=0,d=[];f<i.length;f++)a=i[f],Object.prototype.hasOwnProperty.call(r,a)&&r[a]&&d.push(r[a][0]),r[a]=0;for(s in c)Object.prototype.hasOwnProperty.call(c,s)&&(e[s]=c[s]);l&&l(t);while(d.length)d.shift()();return o.push.apply(o,u||[]),n()}function n(){for(var e,t=0;t<o.length;t++){for(var n=o[t],s=!0,i=1;i<n.length;i++){var c=n[i];0!==r[c]&&(s=!1)}s&&(o.splice(t--,1),e=a(a.s=n[0]))}return e}var s={},r={index:0},o=[];function a(t){if(s[t])return s[t].exports;var n=s[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,a),n.l=!0,n.exports}a.m=e,a.c=s,a.d=function(e,t,n){a.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},a.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},a.t=function(e,t){if(1&t&&(e=a(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(a.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var s in e)a.d(n,s,function(t){return e[t]}.bind(null,s));return n},a.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return a.d(t,"a",t),t},a.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},a.p="/static/dist/";var i=window["webpackJsonp"]=window["webpackJsonp"]||[],c=i.push.bind(i);i.push=t,i=i.slice();for(var u=0;u<i.length;u++)t(i[u]);var l=c;o.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("56d7")},"034f":function(e,t,n){"use strict";n("85ec")},"56d7":function(e,t,n){"use strict";n.r(t);n("e260"),n("e6cf"),n("cca6"),n("a79d");var s=n("2b0e"),r=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("v-app",[n("main",{staticClass:"container mt-5 p-5"},[n("router-view")],1)])},o=[],a=(n("034f"),n("2877")),i={},c=Object(a["a"])(i,r,o,!1,null,null,null),u=c.exports,l=(n("ac1f"),n("5319"),n("8c4f")),f=n("2f62"),d=(n("d3b7"),n("99af"),n("07ac"),n("bc3a")),m=n.n(d),p=m.a.create({baseURL:"/api/v1/",timeout:5e3,headers:{"Content-Type":"application/json","X-Requested-With":"XMLHttpRequest"}});p.interceptors.request.use((function(e){w.dispatch("message/clearMessages");var t=localStorage.getItem("access");return t?(e.headers.Authorization="JWT "+t,e):e}),(function(e){return Promise.reject(e)})),p.interceptors.response.use((function(e){return e}),(function(e){console.log("error.response=",e.response);var t,n=e.response?e.response.status:500;if(400===n){var s=[].concat.apply([],Object.values(e.response.data));w.dispatch("message/setWarningMessages",{messages:s})}else if(401===n){var r=localStorage.getItem("access");t=null!=r?"ログイン有効期限切れ":"認証エラー",w.dispatch("auth/logout"),w.dispatch("message/setErrorMessage",{message:t})}else 403===n?(t="権限エラーです。",w.dispatch("message/setErrorMessage",{message:t})):(t="想定外のエラーです。",w.dispatch("message/setErrorMessage",{message:t}));return Promise.reject(e)}));var g=p;s["default"].use(f["a"]);var h={namespaced:!0,state:{username:"",isLoggedIn:!1},mutations:{set:function(e,t){e.username=t.user.username,e.isLoggedIn=!0},clear:function(e){e.username="",e.isLoggedIn=!1}},actions:{login:function(e,t){return g.post("/auth/jwt/create/",{username:t.username,password:t.password}).then((function(t){return localStorage.setItem("access",t.data.access),e.dispatch("renew")}))},logout:function(e){localStorage.removeItem("access"),e.commit("clear")},renew:function(e){return g.get("/auth/users/me/").then((function(t){var n=t.data;e.commit("set",{user:n})}))}}},v={namespaced:!0,state:{error:"",warnings:[],info:""},mutations:{set:function(e,t){t.error&&(e.error=t.error),t.warnings&&(e.warnings=t.warnings),t.info&&(e.info=t.info)},clear:function(e){e.error="",e.warnings=[],e.info=""}},actions:{setErrorMessage:function(e,t){e.commit("clear"),e.commit("set",{error:t.message})},setWarningMessages:function(e,t){e.commit("clear"),e.commit("set",{warnings:t.messages})},setInfoMessage:function(e,t){e.commit("clear"),e.commit("set",{info:t.message})},clearMessages:function(e){e.commit("clear")}}},b=new f["a"].Store({modules:{auth:h,message:v}}),w=b,y=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{attrs:{id:"login-page"}},[n("p",{staticClass:"h5 mb-5"},[e._v("Login")]),n("v-form",{ref:"form",attrs:{"lazy-validation":""},model:{value:e.valid,callback:function(t){e.valid=t},expression:"valid"}},[n("v-text-field",{attrs:{counter:10,rules:e.usernameRules,label:"Name",required:""},model:{value:e.username,callback:function(t){e.username=t},expression:"username"}}),n("v-text-field",{attrs:{rules:e.passwordRules,label:"Password",type:"password",required:""},model:{value:e.password,callback:function(t){e.password=t},expression:"password"}}),n("v-btn",{staticClass:"mt-4",attrs:{disabled:!e.valid,color:"primary",block:""},on:{click:e.validate}},[e._v(" Login ")])],1)],1)},x=[],I={data:function(){return{valid:!0,username:"",usernameRules:[function(e){return!!e||"ユーザー名を入力してください。"},function(e){return e&&e.length<=10||"ユーザー名は10文字以内です。"}],password:"",passwordRules:[function(e){return!!e||"パスワードを入力してください。"},function(e){return e&&e.length<=10||"パスワードは10文字以内です。"}]}},methods:{validate:function(){this.$refs.form.validate()&&this.submitLogin()},reset:function(){this.$refs.form.reset()},resetValidation:function(){this.$refs.form.resetValidation()},submitLogin:function(){var e=this;this.$store.dispatch("auth/login",{username:this.username,password:this.password}).then((function(){console.log("Login succeeded."),e.$store.dispatch("message/setInfoMessage",{message:"ログインしました。"});var t=e.$route.query.next||"/";e.$router.replace(t)}))}}},M=I,_=Object(a["a"])(M,y,x,!1,null,"37d48bc5",null),j=_.exports,P=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"home"},[n("PostInfo")],1)},O=[],S=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"post-info"},[n("v-card",[n("v-card-title",[e._v("お知らせ投稿一覧")]),n("v-data-table",{staticClass:"elevation-0",attrs:{headers:e.headers,items:e.formattedPosts},scopedSlots:e._u([{key:"item.edit",fn:function(t){var s=t.item;return[n("v-icon",{staticClass:"mr-2",attrs:{small:""},on:{click:function(t){return e.editItem(s)}}},[e._v(" mdi-pencil ")])]}},{key:"item.delete",fn:function(t){var s=t.item;return[n("v-icon",{attrs:{small:""},on:{click:function(t){return e.deleteItem(s)}}},[e._v(" mdi-delete ")])]}}])})],1)],1)},L=[];n("159b");function k(e,t){return e=new Date(e),t=t.replace(/YYYY/,e.getFullYear()),t=t.replace(/MM/,e.getMonth()+1),t=t.replace(/DD/,e.getDate()),t}var $=k,E={name:"PostInfo",computed:{formattedPosts:function(){var e=[];return this.posts.forEach((function(t){e.push({id:t.id,title:t.title,published:$(t.published,"YYYY年MM月DD日"),edit:"edit",delete:"delete"})})),e}},data:function(){return{headers:[{text:"投稿日時",align:"start",sortable:!1,value:"published"},{text:"投稿タイトル",value:"title"},{text:"編集",value:"edit"},{text:"削除",value:"delete"}],posts:[]}},methods:{fetchItems:function(){var e=this;this.posts=[],g.get("/news/").then((function(t){e.posts=t.data})).catch((function(e){console.log(e)}))},editItem:function(e){console.log(e)},deleteItem:function(e){console.log(e),g.delete("/news/".concat(e.id,"/")).then(this.fetchItems()).catch((function(e){console.log(e)}))}},created:function(){this.fetchItems()}},q=E,Y=Object(a["a"])(q,S,L,!1,null,"b7ed9c9c",null),C=Y.exports,R={name:"Home",components:{PostInfo:C}},D=R,T=Object(a["a"])(D,P,O,!1,null,null,null),A=T.exports;s["default"].use(l["a"]);var W=[{path:"/login",name:"LoginPage",component:j},{path:"/",name:"Home",component:A,meta:{requiresAuth:!0}},{path:"/:catchAll(.*)",redirect:"/"}],H=new l["a"]({mode:"history",base:"/owner/",routes:W});function J(e){console.log("Force to login page."),H.replace({path:"/login",query:{next:e.fullPath}})}H.beforeEach((function(e,t,n){var s=w.state.auth.isLoggedIn,r=localStorage.getItem("access");console.log("to.path=",e.path),console.log("isLoggedIn=",s),e.matched.some((function(e){return e.meta.requiresAuth}))?s?(console.log("User is already logged in. So, free to next."),n()):(console.log("User is not logged in."),null!=r?(console.log("Try to renew user info."),w.dispatch("auth/renew").then((function(){console.log("Succeeded to renew. So, free to next."),n()})).catch((function(){J(e)}))):J(e)):(console.log("Go to public page."),n())}));var U=H,z=n("ce5b"),F=n.n(z);n("bf40");s["default"].use(F.a);var V={},X=new F.a(V),G=n("5f5b");n("f9e3"),n("2dd8");s["default"].use(G["a"]),s["default"].config.productionTip=!1,new s["default"]({bootstrap:void 0,vuetify:X,router:U,store:w,render:function(e){return e(u)}}).$mount("#app")},"85ec":function(e,t,n){}});
//# sourceMappingURL=index.dd02e265.js.map