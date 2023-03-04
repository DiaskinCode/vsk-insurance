<template>
  <header class="header container-wrapper bb-1 bg-w pos-f">
    <div class="header__content container jc-sb ai-c py-20 py-15-mb">
      <AppLogo
        class="header__logo"
      />
      <AppNav
        class="d-n-mb"
        :links="links"
      />
      <AppMenuButton
        :is-open="isOpen"
        @click="openMenu"
      />
      <AppMenu
        :links="links"
        :is-open="isOpen"
        @close="openMenu"
      />
    </div>
  </header>
</template>

<script>
export default {
  name: 'TheHeader',
  props: {},
  data: () => ({
    isOpen: false,
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
  methods: {
    openMenu() {
      this.isOpen = !this.isOpen;
      this.setBodyOverflow(this.isOpen);
    },
    setBodyOverflow(hidden) {
      document.body.style.overflow = hidden ? 'hidden' : '';
    },
  },
}
</script>

<style lang="scss">
.header {
  border-color: #F3F3F5;
  /* .header__logo */
  &__logo {
    margin: -1rem 0;
    @media (max-width: 600px) {
      margin: 0;
    }
  }
}
</style>
