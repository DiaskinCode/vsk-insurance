<template>
  <img
    class="app-logo"
    src="/logo.png"
    alt="ВСК"
  >
</template>

<script>
export default {
  name: 'AppLogo',
  props: {
    src: {
      type: String,
      default: '/logo.png'
    }
  },
  data: () => ({
  }),
  computed: {},
  methods: {},

}
</script>

<style lang="scss">
.app-logo {
  width: 18.4rem;
  height: 4.8rem;
  @media (max-width: 600px) {
    width: 8.5rem;
    height: 2.14rem;
  }
}
</style>
