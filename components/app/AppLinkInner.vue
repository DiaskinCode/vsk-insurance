<template>
  <a
    class="app-inner-link td-u cur-p c-i"
    :href="href"
    target="_blanc"
  ><slot>{{ text }}</slot></a>
</template>

<script>
export default {
  name: 'AppLinkInnner',
  props: {
    href: {
      type: String,
      default: '',
    },
    text: {
      type: String,
      default: '',
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
