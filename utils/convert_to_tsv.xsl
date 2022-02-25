<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="text" version="1.0" encoding="UTF-8" indent="no"/>
  <xsl:strip-space elements="s"/>

  <xsl:variable name="newline">
    <xsl:text>
</xsl:text>
  </xsl:variable>

  <xsl:template match="/">
      <xsl:for-each select="//s">
	<!-- <xsl:copy-of select="."/> -->
	<xsl:value-of select='substring(., 2)'/>
	<xsl:value-of select="$newline"/>
      </xsl:for-each>
  </xsl:template>

</xsl:stylesheet>
