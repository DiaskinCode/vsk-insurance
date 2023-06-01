<template>
  <Button
    class="
      app-button
      c-w bg-p py-15 px-30 br-15 fw-7 fs-22 lh-120
      fs-16-mb px-15-mb
    "
    :class="{ 'app-button--secondary': secondary }"
    v-bind="$attrs"
    v-on="$listeners"
  />
</template>

<script>
export default {
  name: 'AppButton',
  props: {
    secondary: {
      type: Boolean,
      default: false,
    },
  },
  data: () => ({
  }),
  computed: {
  },
  methods: {
  },
};
</script>

<style lang="scss">
.app-button {
  &:disabled {
    opacity: .5;
  }
  &--secondary {
    color: $primary;
    background: $secondary;
  }

  .p-button-icon-left {
    margin-right: .5rem;
  }
}
</style>
