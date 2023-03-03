<template>
  <a
    class="nav-link fs-15 lh-190 us-n"
    :class="{
      'nav-link--button lh-120 fw-7 c-p py-5 px-15 br-10': button,
    }"
    :href="href"
    @click="onClick"
  >
    {{ label }}
  </a>
</template>

<script>
export default {
  name: 'AppNavLink',
  props: {
    label: {
      type: String,
      default: '',
    },
    href: {
      type: String,
      default: '',
    },
    button: {
      type: Boolean,
      default: false,
    },
  },
  data: () => ({
  }),
  computed: {},
  methods: {
    onClick(event) {
      this.$emit('click', event);
    },
  },

}
</script>

<style lang="scss">
.nav-link {
  cursor: pointer;
  /* .nav-link--button */
  &--button {
    background: #EEF9FF;
  }
}
</style>
