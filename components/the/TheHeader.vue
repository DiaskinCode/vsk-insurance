<template>
  <header class="header container-wrapper bb-1">
    <div class="header__content container jc-sb py-20">
      <AppLogo
        class="header__logo"
      />
      <AppNav
        :links="links"
      />
    </div>
  </header>
</template>

<script>
export default {
  name: 'TheHeader',
  props: {},
  data: () => ({
    links: [
      {
        href: '#include',
        label: 'Что включает полис',
      },
      {
        href: '#benefit',
        label: 'Преимущества',
      },
      {
        href: '#question',
        label: 'FAQ',
      },
      {
        href: '#insurance',
        label: 'Рассчитать',
        button: true,
      },
    ]
  }),
  computed: {},
  methods: {},
}
</script>

<style lang="scss">
.header {
  border-color: #F3F3F5;
  /* .header__logo */
  &__logo {
    margin: -1rem 0;
  }
}
</style>
