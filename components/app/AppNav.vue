<template>
  <nav class="app-nav d-f ai-c fd-c-mb row gx-40">
    <AppNavLink
      v-for="(link, i) in links"
      :key="i"
      :label="link.label"
      :href="link.href"
      :button="link.button"
      @click="onClick"
    />
  </nav>
</template>

<script>
export default {
  name: 'AppNav',
  props: {
    links: {
      type: Array,
      required: true,
    },
  },
  data: () => ({
  }),
  computed: {},
  methods: {},
}
</script>

<style lang="scss">
</style>
