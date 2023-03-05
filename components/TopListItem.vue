<template>
  <div class="top-list-item d-f ai-fs">
    <img
      class="top-list-item__check mr-15"
      src="/check.svg"
      alt="check"
    >
    <div>
      <slot />
    </div>
  </div>
</template>

<script>
export default {
  name: 'TopListItem',
  props: {},
  data: () => ({
  }),
  computed: {},
  methods: {},
}
</script>

<style lang="scss">
.top-list-item {
  /* .top-list-item__check */
  &__check {
    margin-top: .65rem;
    width: 2.5rem;
    height: 1.7rem;
  }
}

</style>
