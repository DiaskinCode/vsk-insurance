<template>
  <div
    class="
      benefit-list-item
      d-f ai-c bg-w bs-1 br-30 p-30 py-10
      fd-c-mb ai-fs-mb br-10-mb p-20-mb
    "
  >
    <div class="benefit-list-item__img-wrapper mr-40 mb-10-mb">
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
  /* .benefit-list-item__img-wrapper */
  &__img-wrapper {
    margin-top: -2.5rem;
    @media (max-width: 600px) {
      margin-top: -5.5rem;
    }
  }
  /* .benefit-list-item__img */
  &__img {
    width: 15rem;
    height: 16.75rem;
    @media (max-width: 600px) {
      width: 9.5rem;
      height: 10.5rem;
    }
  }
}
</style>
