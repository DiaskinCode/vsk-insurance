<template>
  <nav class="app-nav d-f ai-c fd-c-mb">
    <AppNavLink
      v-for="(link, i) in links"
      :key="i"
      class="ml-40"
      :label="link.label"
      :href="link.href"
      :button="link.button"
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
  methods: {
  },
}
</script>

<style lang="scss">
</style>
