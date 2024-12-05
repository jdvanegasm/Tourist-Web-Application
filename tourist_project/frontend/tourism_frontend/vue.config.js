module.exports = {
  configureWebpack: {
    resolve: {
      alias: {
        '@vue/runtime-core': require.resolve('@vue/runtime-core'),
      },
    },
  },
  chainWebpack(config) {
    config.plugin('define').tap((args) => {
      args[0]['__VUE_PROD_HYDRATION_MISMATCH_DETAILS__'] = JSON.stringify(false);
      return args;
    });
  },
};
