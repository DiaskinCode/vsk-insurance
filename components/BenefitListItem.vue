<template>
  <div class="benefit-list-item d-f ai-c bg-w bs-1 br-30 p-30">
    <div class="mr-20">
      <img
        class="benefit-list-item__img"
        :src="src"
        alt="benefit"
      >
    </div>
    <div>
      <slot />
    </div>
  </div>
</template>

<script>
export default {
  name: 'BenefitListItem',
  props: {
    src: {
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
.benefit-list-item {
  /* .benefit-list-item__img */
  &__img {
    width: 16.835rem;
    height: 13.013rem;
  }
}
</style>
