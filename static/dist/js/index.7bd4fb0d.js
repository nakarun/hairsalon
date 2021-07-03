(function(e){function t(t){for(var s,o,i=t[0],c=t[1],u=t[2],f=0,d=[];f<i.length;f++)o=i[f],Object.prototype.hasOwnProperty.call(r,o)&&r[o]&&d.push(r[o][0]),r[o]=0;for(s in c)Object.prototype.hasOwnProperty.call(c,s)&&(e[s]=c[s]);l&&l(t);while(d.length)d.shift()();return a.push.apply(a,u||[]),n()}function n(){for(var e,t=0;t<a.length;t++){for(var n=a[t],s=!0,i=1;i<n.length;i++){var c=n[i];0!==r[c]&&(s=!1)}s&&(a.splice(t--,1),e=o(o.s=n[0]))}return e}var s={},r={index:0},a=[];function o(t){if(s[t])return s[t].exports;var n=s[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,o),n.l=!0,n.exports}o.m=e,o.c=s,o.d=function(e,t,n){o.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},o.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},o.t=function(e,t){if(1&t&&(e=o(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(o.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var s in e)o.d(n,s,function(t){return e[t]}.bind(null,s));return n},o.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return o.d(t,"a",t),t},o.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},o.p="/static/dist/";var i=window["webpackJsonp"]=window["webpackJsonp"]||[],c=i.push.bind(i);i.push=t,i=i.slice();for(var u=0;u<i.length;u++)t(i[u]);var l=c;a.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("56d7")},"034f":function(e,t,n){"use strict";n("85ec")},"56d7":function(e,t,n){"use strict";n.r(t);n("e260"),n("e6cf"),n("cca6"),n("a79d");var s=n("2b0e"),r=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("v-app",[n("main",{staticClass:"container mt-5 p-5"},[n("router-view")],1)])},a=[],o=(n("034f"),n("2877")),i={},c=Object(o["a"])(i,r,a,!1,null,null,null),u=c.exports,l=n("8c4f"),f=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{attrs:{id:"login-page"}},[n("p",{staticClass:"h5 mb-5"},[e._v("Login")]),n("v-form",{ref:"form",attrs:{"lazy-validation":""},model:{value:e.valid,callback:function(t){e.valid=t},expression:"valid"}},[n("v-text-field",{attrs:{counter:10,rules:e.usernameRules,label:"Name",required:""},model:{value:e.username,callback:function(t){e.username=t},expression:"username"}}),n("v-text-field",{attrs:{rules:e.passwordRules,label:"Password",type:"password",required:""},model:{value:e.password,callback:function(t){e.password=t},expression:"password"}}),n("v-btn",{staticClass:"mt-4",attrs:{disabled:!e.valid,color:"primary",block:""},on:{click:e.validate}},[e._v(" Login ")])],1)],1)},d=[],m=(n("ac1f"),n("5319"),{data:function(){return{valid:!0,username:"",usernameRules:[function(e){return!!e||"ユーザー名を入力してください。"},function(e){return e&&e.length<=10||"ユーザー名は10文字以内です。"}],password:"",passwordRules:[function(e){return!!e||"パスワードを入力してください。"},function(e){return e&&e.length<=10||"パスワードは10文字以内です。"}]}},methods:{validate:function(){this.$refs.form.validate()&&this.submitLogin()},reset:function(){this.$refs.form.reset()},resetValidation:function(){this.$refs.form.resetValidation()},submitLogin:function(){var e=this;this.$store.dispatch("auth/login",{username:this.username,password:this.password}).then((function(){console.log("Login succeeded."),e.$store.dispatch("message/setInfoMessage",{message:"ログインしました。"});var t=e.$route.query.next||"/";e.$router.replace(t)}))}}}),p=m,g=Object(o["a"])(p,f,d,!1,null,"37d48bc5",null),h=g.exports,v=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"home"},[n("PostInfo")],1)},b=[],w=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"post-info"},[n("v-card",[n("v-card-title",[e._v("お知らせ投稿一覧")]),n("v-data-table",{staticClass:"elevation-0",attrs:{headers:e.headers,items:e.formattedPosts},scopedSlots:e._u([{key:"item.edit",fn:function(t){var s=t.item;return[n("v-icon",{staticClass:"mr-2",attrs:{small:""},on:{click:function(t){return e.editItem(s)}}},[e._v(" mdi-pencil ")])]}},{key:"item.delete",fn:function(t){var s=t.item;return[n("v-icon",{attrs:{small:""},on:{click:function(t){return e.deleteItem(s)}}},[e._v(" mdi-delete ")])]}}])})],1)],1)},y=[],_=(n("159b"),n("d3b7"),n("99af"),n("07ac"),n("bc3a")),x=n.n(_),I=n("2f62");s["default"].use(I["a"]);var M={namespaced:!0,state:{username:"",isLoggedIn:!1},mutations:{set:function(e,t){e.username=t.user.username,e.isLoggedIn=!0},clear:function(e){e.username="",e.isLoggedIn=!1}},actions:{login:function(e,t){return k.post("/auth/jwt/create/",{username:t.username,password:t.password}).then((function(t){return localStorage.setItem("access",t.data.access),e.dispatch("renew")}))},logout:function(e){localStorage.removeItem("access"),e.commit("clear")},renew:function(e){return k.get("/auth/users/me/").then((function(t){var n=t.data;e.commit("set",{user:n})}))}}},O={namespaced:!0,state:{error:"",warnings:[],info:""},mutations:{set:function(e,t){t.error&&(e.error=t.error),t.warnings&&(e.warnings=t.warnings),t.info&&(e.info=t.info)},clear:function(e){e.error="",e.warnings=[],e.info=""}},actions:{setErrorMessage:function(e,t){e.commit("clear"),e.commit("set",{error:t.message})},setWarningMessages:function(e,t){e.commit("clear"),e.commit("set",{warnings:t.messages})},setInfoMessage:function(e,t){e.commit("clear"),e.commit("set",{info:t.message})},clearMessages:function(e){e.commit("clear")}}},j=new I["a"].Store({modules:{auth:M,message:O}}),P=j,E=x.a.create({baseURL:Object({NODE_ENV:"production",BASE_URL:"/static/dist/"}).VUE_APP_ROOT_API,timeout:5e3,headers:{"Content-Type":"application/json","X-Requested-With":"XMLHttpRequest"}});E.interceptors.request.use((function(e){P.dispatch("message/clearMessages");var t=localStorage.getItem("access");return t?(e.headers.Authorization="JWT "+t,e):e}),(function(e){return Promise.reject(e)})),E.interceptors.response.use((function(e){return e}),(function(e){console.log("error.response=",e.response);var t,n=e.response?e.response.status:500;if(400===n){var s=[].concat.apply([],Object.values(e.response.data));P.dispatch("message/setWarningMessages",{messages:s})}else if(401===n){var r=localStorage.getItem("access");t=null!=r?"ログイン有効期限切れ":"認証エラー",P.dispatch("auth/logout"),P.dispatch("message/setErrorMessage",{message:t})}else 403===n?(t="権限エラーです。",P.dispatch("message/setErrorMessage",{message:t})):(t="想定外のエラーです。",P.dispatch("message/setErrorMessage",{message:t}));return Promise.reject(e)}));var k=E;function L(e,t){return e=new Date(e),t=t.replace(/YYYY/,e.getFullYear()),t=t.replace(/MM/,e.getMonth()+1),t=t.replace(/DD/,e.getDate()),t}var S=L,$={name:"PostInfo",computed:{formattedPosts:function(){var e=[];return this.posts.forEach((function(t){e.push({id:t.id,title:t.title,published:S(t.published,"YYYY年MM月DD日"),edit:"edit",delete:"delete"})})),e}},data:function(){return{headers:[{text:"投稿日時",align:"start",sortable:!1,value:"published"},{text:"投稿タイトル",value:"title"},{text:"編集",value:"edit"},{text:"削除",value:"delete"}],posts:[]}},methods:{fetchItems:function(){var e=this;this.posts=[],k.get("/news/").then((function(t){e.posts=t.data})).catch((function(e){console.log(e)}))},editItem:function(e){console.log(e)},deleteItem:function(e){console.log(e),k.delete("/news/".concat(e.id,"/")).then(this.fetchItems()).catch((function(e){console.log(e)}))}},created:function(){this.fetchItems()}},R=$,Y=Object(o["a"])(R,w,y,!1,null,"b7ed9c9c",null),C=Y.exports,D={name:"Home",components:{PostInfo:C}},q=D,T=Object(o["a"])(q,v,b,!1,null,null,null),A=T.exports;s["default"].use(l["a"]);var V=[{path:"/owner/login",name:"LoginPage",component:h},{path:"/owner",name:"Home",component:A}],W=new l["a"]({mode:"history",base:"/static/dist/",routes:V}),H=W,J=n("ce5b"),N=n.n(J);n("bf40");s["default"].use(N.a);var U={},z=new N.a(U),X=n("5f5b");n("f9e3"),n("2dd8");s["default"].use(X["a"]),s["default"].config.productionTip=!1,new s["default"]({bootstrap:void 0,vuetify:z,router:H,store:P,render:function(e){return e(u)}}).$mount("#app")},"85ec":function(e,t,n){}});
//# sourceMappingURL=index.7bd4fb0d.js.map