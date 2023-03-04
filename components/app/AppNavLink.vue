<template>
  <a
    class="nav-link us-n"
    :class="{
      'nav-link--button lh-120 fw-7 c-p py-5 px-15 br-10': button,
    }"
    :href="href"
  >
    <AppButton
      class="nav-link__button"
      :class="{
        'nav-link__button--primary': button,
      }"
      :label="label"
      @click="onClick"
    />
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
  }
  /* .nav-link__button */
  &__button {
    background: none;
    color: $black;
    line-height: 190%;
    font-size: 1.5rem;
    font-weight: 400;
    padding: 0;
  }
  &__button--primary {
    background: #EEF9FF;
    color: $primary;
    line-height: 120%;
    font-weight: 700;
    padding: 1rem 1.5rem;
    border-radius: 1rem;
  }
}
</style>
