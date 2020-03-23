<template>
  <div class="query">
    <div class="dropdown">
      <el-dropdown trigger="click" placement="bottom-start">
        <span class="el-dropdown-link">
          {{title}}
          <i class="el-icon-caret-bottom el-icon--right"></i>
        </span>
        <el-dropdown-menu slot="dropdown" class="onDropdown">
          <el-dropdown-item
            @click.native="onDropdown(index)"
            v-for="(item,index) in dropdownList"
            :key="index"
          >{{item}}</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      dropdownList: [
        "单一账户查询",
        "账户间关联性查询",
        "公链交易查询",
        "公链交易量及走势查询",
        "交易所账户查询"
      ]
    };
  },
  computed: {
    title() {
      return this.$store.state.queryTitle;
    }
  },
  mounted() {
    let that = this;
    let url = this.$route.path;
    this.$store.commit("changeIndexNum", 1);
    console.log(url);
    if (url == "/singleAccount") {
      that.$store.commit("changeQueryTitle", this.dropdownList[0]);
    } else if (url == "/relevance") {
      that.$store.commit("changeQueryTitle", this.dropdownList[1]);
    } else if (url == "/transaction") {
      that.$store.commit("changeQueryTitle", this.dropdownList[2]);
    } else if (url == "/trendChart") {
      that.$store.commit("changeQueryTitle", this.dropdownList[3]);
    } else if (url == "/exchange") {
      that.$store.commit("changeQueryTitle", this.dropdownList[4]);
    }
  },

  methods: {
    onDropdown(index) {
      let that = this;
      that.$store.commit("changeQueryTitle", this.dropdownList[index]);
      this.$store.commit("changeQueryIndex", index);
      let list = [
        "singleAccount",
        "relevance",
        "transaction",
        "trendChart",
        "exchange"
      ];

      this.$router.push({ path: `/${list[index]}` });
    }
  }
};
</script>


<style lang="less">
:focus {
  outline: 0;
}
.onDropdown {
  width: 338px;
}
.el-dropdown-menu {
  background-color: #0f152c;
  box-shadow: 0px 3px 6px 0px rgba(0, 0, 0, 0.16);
  border: none;
  padding: 0;
  overflow: hidden;
  box-sizing: border-box;
  margin-bottom: 0;
  border-radius: 5px;
}
.el-popper .popper__arrow {
  display: none;
}
.el-dropdown-menu__item {
  height: 60px;
  line-height: 60px;
  box-sizing: border-box;
  color: #a1a5c5;
  font-size: 14px;
  border-bottom: solid 1px #1f3e5a;
}

.border:last-child {
  border-bottom: none;
}
.el-dropdown-menu__item:focus,
.el-dropdown-menu__item:not(.is-disabled):hover {
  background-color: #0f152c;
  color: #00ce7d;
}
.query {
  width: 1228px;
  margin: 0 auto;
  .dropdown {
    width: 100%;
    background-color: #1c324a;
    margin: 24px 0 0 0;
    opacity: 0.8;
    height: 54px;
    line-height: 54px;
    padding-left: 10px;
    box-sizing: border-box;
    .el-dropdown {
      font-size: 18px;
      color: #ffffff;
    }
  }
}
</style>
